import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host     = os.getenv("DB_HOST",     "localhost"),
        dbname   = os.getenv("DB_NAME",     "india_bike_analysis"),
        user     = os.getenv("DB_USER",     "postgres"),
        password = os.getenv("DB_PASSWORD", "")
    )

def run_query(sql):
    conn = get_connection()
    df   = pd.read_sql(sql, conn)
    conn.close()
    return df

def load_bikes():
    return run_query("SELECT * FROM dim_bikes")

def load_sales():
    return run_query("SELECT * FROM sales_monthly")

def load_ev_states():
    return run_query("SELECT * FROM ev_states")

def load_reviews():
    return run_query("SELECT * FROM reviews")