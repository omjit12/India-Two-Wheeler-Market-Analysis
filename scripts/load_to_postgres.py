import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:om*7489@localhost:5432/india_bike_analysis"
engine = create_engine(DB_URL)

MASTER = "data/master"

# ── Load raw tables ───────────────────────────────────────────────────────────
tables = {
    "bikes_master" : f"{MASTER}/master_bike_data.csv",
    "sales_monthly": f"{MASTER}/sales_monthly.csv",
    "ev_states"    : f"{MASTER}/ev_states.csv",
    "reviews"      : f"{MASTER}/reviews.csv",
}

for table_name, filepath in tables.items():
    df = pd.read_csv(filepath)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"✅ {table_name:20s} → {len(df):>5} rows, {len(df.columns):>2} cols")

# ── Create clean dim_bikes (unique bikes only — 66 rows) ──────────────────────
with engine.connect() as conn:

    # dim_bikes — deduplicated, 66 rows, bike_id is unique here
    conn.execute(text("DROP TABLE IF EXISTS dim_bikes;"))
    conn.execute(text("""
        CREATE TABLE dim_bikes AS
        SELECT DISTINCT ON (bike_id)
            bike_id, brand_id, name, brand, segment, fuel_type,
            is_ev, price_inr, engine_cc, power_bhp, torque_nm,
            mileage_kmpl, weight_kg, top_speed_kmph,
            battery_kwh, range_km, launch_year, rating
        FROM bikes_master
        ORDER BY bike_id;
    """))
    conn.execute(text("ALTER TABLE dim_bikes ADD PRIMARY KEY (bike_id);"))
    print("\n✅ dim_bikes created  → unique 66 rows, bike_id is PRIMARY KEY")

    # Indexes on fact tables
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_sales_bike_id    ON sales_monthly(bike_id);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_sales_brand_id   ON sales_monthly(brand_id);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_sales_year       ON sales_monthly(year);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_reviews_bike_id  ON reviews(bike_id);"))
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_reviews_brand_id ON reviews(brand_id);"))
    conn.commit()
    print("✅ Indexes created on sales_monthly and reviews")

    # ── Test queries ──────────────────────────────────────────────────────────
    print("\n--- Test 1: dim_bikes check ---")
    result = pd.read_sql("""
        SELECT segment,
               COUNT(bike_id)         AS total_bikes,
               ROUND(AVG(price_inr))  AS avg_price
        FROM dim_bikes
        GROUP BY segment
        ORDER BY total_bikes DESC
    """, conn)
    print(result.to_string(index=False))

    print("\n--- Test 2: Top 5 brands by 2023 sales ---")
    result = pd.read_sql("""
        SELECT d.brand,
               SUM(s.units_sold) AS total_units_2023
        FROM dim_bikes d
        JOIN sales_monthly s ON d.bike_id = s.bike_id
        WHERE s.year = 2023
        GROUP BY d.brand
        ORDER BY total_units_2023 DESC
        LIMIT 5
    """, conn)
    print(result.to_string(index=False))

    print("\n--- Test 3: EV vs Petrol market share 2023 ---")
    result = pd.read_sql("""
        SELECT d.fuel_type,
               SUM(s.units_sold) AS total_units,
               ROUND(SUM(s.units_sold) * 100.0 /
                     SUM(SUM(s.units_sold)) OVER (), 2) AS market_share_pct
        FROM dim_bikes d
        JOIN sales_monthly s ON d.bike_id = s.bike_id
        WHERE s.year = 2023
        GROUP BY d.fuel_type
    """, conn)
    print(result.to_string(index=False))

print("\n✅ PostgreSQL fully loaded and ready!")