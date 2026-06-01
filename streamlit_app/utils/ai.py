import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def get_data_context(bikes_df, sales_df):
    sales_summary = sales_df.groupby(
        ["name","year"])["units_sold"].sum().reset_index()
    top_bikes = sales_summary.sort_values(
        "units_sold", ascending=False).head(20)

    ev_bikes = bikes_df[bikes_df["is_ev"] == True][[
        "name","brand","price_inr","range_km","battery_kwh"
    ]]

    petrol_bikes = bikes_df[bikes_df["is_ev"] == False][[
        "name","brand","segment","price_inr","mileage_kmpl","power_bhp"
    ]]

    context = f"""
You are an expert data analyst specialising in India's two-wheeler market.
You have access to a comprehensive dataset with the following details:

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

=== PRICE SEGMENTS ===
Budget  (under Rs 80,000)      : {len(bikes_df[bikes_df['price_inr'] < 80000])} bikes
Mid     (Rs 80,000 - 1,50,000) : {len(bikes_df[(bikes_df['price_inr'] >= 80000) & (bikes_df['price_inr'] < 150000)])} bikes
Premium (Rs 1,50,000 - 2,50,000): {len(bikes_df[(bikes_df['price_inr'] >= 150000) & (bikes_df['price_inr'] < 250000)])} bikes
Luxury  (above Rs 2,50,000)    : {len(bikes_df[bikes_df['price_inr'] >= 250000])} bikes

=== EV MARKET GROWTH ===
2019: ~0%    2020: ~0.1%    2021: ~0.5%
2022: ~2%    2023: ~10.6%

=== KEY MARKET INSIGHTS ===
- Hero MotoCorp leads with ~32% market share
- Honda Activa 6G is India's best selling scooter
- Hero Splendor Plus is India's best selling motorcycle
- Commuter segment dominates with 60M+ units
- Maharashtra leads EV adoption among all states
- EV running cost is Rs 0.2/km vs Rs 1.6-3.5/km for petrol
- Ultraviolette F77 has best EV range at 307km
- KTM dominates performance segment

INSTRUCTIONS:
- Answer based on this data only
- Always use specific numbers and bike names
- Be concise, insightful and helpful
- Format your response clearly with headers when needed
- If asked to compare, give a clear winner with reasoning
- Use Rs instead of the rupee symbol
"""
    return context


def ask_gemini(question, context):
    prompt = f"{context}\n\nUser Question: {question}\n\nProvide a clear, data-driven answer:"
    response = model.generate_content(prompt)
    return response.text


def get_recommendation(budget_min, budget_max, usage,
                        fuel_pref, priority, rider_exp, bikes_df):
    filtered = bikes_df[
        (bikes_df["price_inr"] >= budget_min) &
        (bikes_df["price_inr"] <= budget_max)
    ].copy()

    if fuel_pref == "Electric":
        filtered = filtered[filtered["is_ev"] == True]
    elif fuel_pref == "Petrol":
        filtered = filtered[filtered["is_ev"] == False]

    if len(filtered) == 0:
        return "No bikes found matching your criteria. Please adjust your budget or fuel preference."

    bike_list = filtered[[
        "name","brand","segment","fuel_type",
        "price_inr","power_bhp","mileage_kmpl",
        "range_km","rating","weight_kg"
    ]].sort_values("price_inr").to_string(index=False)

    prompt = f"""
You are India's top motorcycle expert helping a customer choose the perfect bike.

=== CUSTOMER PROFILE ===
Budget          : Rs {budget_min:,} to Rs {budget_max:,}
Primary Usage   : {usage}
Fuel Preference : {fuel_pref}
Top Priority    : {priority}
Rider Experience: {rider_exp}

=== AVAILABLE BIKES IN BUDGET ===
{bike_list}

=== YOUR TASK ===
Recommend exactly the TOP 3 bikes for this customer.

For each recommendation use this exact format:

## 🏆 Recommendation [1/2/3]: [Bike Name]
**Price:** Rs [price]
**Why perfect for you:** [2-3 sentences specific to their usage and priority]
**Key strength:** [One specific stat or feature]
**One downside:** [Honest limitation]
**Verdict:** [One powerful sentence]

---

After all 3 recommendations add:

## 💡 Pro Tip
[One actionable buying tip specific to their situation]

Be specific, practical and honest. Tailor every word to their exact profile.
"""
    response = model.generate_content(prompt)
    return response.text


def generate_insight(chart_title, data_summary):
    prompt = f"""
You are a data analyst for India's two-wheeler market.

Chart: {chart_title}
Data: {data_summary}

Write exactly 2 sharp sentences of insight.
Be specific with numbers. Focus on the most surprising finding.
No generic statements. Start directly with the insight.
"""
    response = model.generate_content(prompt)
    return response.text