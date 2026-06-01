from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent.parent

def load_bikes():
    return pd.read_csv(BASE_DIR / "data" / "master" / "dim_bikes.csv")

def load_sales():
    return pd.read_csv(BASE_DIR / "data" / "master" / "sales_monthly.csv")

def load_ev_states():
    return pd.read_csv(BASE_DIR / "data" / "master" / "ev_states.csv")

def load_reviews():
    return pd.read_csv(BASE_DIR / "data" / "master" / "reviews.csv")
