import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# API Key
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except Exception:
    api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found in Streamlit Secrets or .env"
    )

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    raise Exception(f"Gemini model initialization failed: {e}")


def get_data_context(bikes_df, sales_df):
    sales_summary = sales_df.groupby(
        ["name", "year"]
    )["units_sold"].sum().reset_index()

    top_bikes = sales_summary.sort_values(
        "units_sold",
        ascending=False
    ).head(20)

    ev_bikes = bikes_df[bikes_df["is_ev"] == True][[
        "name", "brand", "price_inr", "range_km", "battery_kwh"
    ]]

    petrol_bikes = bikes_df[bikes_df["is_ev"] == False][[
        "name", "brand", "segment", "price_inr",
        "mileage_kmpl", "power_bhp"
    ]]

    context = f"""
You are an expert data analyst specialising in India's two-wheeler market.

=== DATASET OVERVIEW ===
Total bikes analysed  : {len(bikes_df)}
EV bikes              : {int(bikes_df['is_ev'].sum())}
Petrol bikes          : {int((~bikes_df['is_ev']).sum())}
Years covered         : 2019 to 2023
Total units sold      : {sales_df['units_sold'].sum():,}
Brands covered        : {bikes_df['brand'].nunique()}
Segments              : {bikes_df['segment'].unique().tolist()}

=== TOP 20 BIKES BY TOTAL SALES (2019-2023) ===
{top_bikes.to_string(index=False)}

=== ALL EV BIKES IN DATASET ===
{ev_bikes.to_string(index=False)}

=== PETROL BIKES (sample) ===
{petrol_bikes.head(20).to_string(index=False)}

=== KEY MARKET INSIGHTS ===
- Hero MotoCorp leads with ~32% market share
- Honda Activa 6G is India's best selling scooter
- Hero Splendor Plus is India's best selling motorcycle
- Maharashtra leads EV adoption among all states
- EV running cost is Rs 0.2/km vs Rs 1.6-3.5/km for petrol

Answer only using this dataset.
Use specific numbers whenever possible.
"""
    return context


def ask_gemini(question, context):
    try:
        prompt = f"""
{context}

User Question:
{question}

Provide a clear, data-driven answer.
"""

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "Gemini returned an empty response."

    except Exception as e:
        return f"""
❌ Gemini Error

{str(e)}

Check:
• GOOGLE_API_KEY in Streamlit Secrets
• Gemini API quota
• Internet connectivity
• Model availability
"""


def get_recommendation(
    budget_min,
    budget_max,
    usage,
    fuel_pref,
    priority,
    rider_exp,
    bikes_df
):
    filtered = bikes_df[
        (bikes_df["price_inr"] >= budget_min) &
        (bikes_df["price_inr"] <= budget_max)
    ].copy()

    if fuel_pref == "Electric":
        filtered = filtered[filtered["is_ev"] == True]
    elif fuel_pref == "Petrol":
        filtered = filtered[filtered["is_ev"] == False]

    if len(filtered) == 0:
        return (
            "No bikes found matching your criteria. "
            "Please adjust your budget or fuel preference."
        )

    bike_list = filtered[[
        "name",
        "brand",
        "segment",
        "fuel_type",
        "price_inr",
        "power_bhp",
        "mileage_kmpl",
        "range_km",
        "rating",
        "weight_kg"
    ]].sort_values("price_inr").to_string(index=False)

    prompt = f"""
Recommend the best 3 bikes.

Budget: Rs {budget_min:,} to Rs {budget_max:,}
Usage: {usage}
Fuel Preference: {fuel_pref}
Priority: {priority}
Experience: {rider_exp}

Available Bikes:
{bike_list}
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "No recommendation generated."

    except Exception as e:
        return f"Recommendation Error: {str(e)}"


def generate_insight(chart_title, data_summary):
    prompt = f"""
Chart: {chart_title}
Data: {data_summary}

Give 2 concise analytical insights.
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "No insight generated."

    except Exception as e:
        return f"Insight Error: {str(e)}"
