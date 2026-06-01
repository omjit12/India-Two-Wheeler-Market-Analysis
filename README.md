# 🏍️ India Two-Wheeler Market Analysis

> A comprehensive end-to-end data analytics project analysing India's two-wheeler market from 2019 to 2023 — covering 66 bikes, 18 brands, 3,936 sales records, and powered by Google Gemini AI.

---

## 🚀 Live Demo

https://india-two-wheeler-market-analysis-fwwu6ue8oucz29ucvj6uva.streamlit.app/

---

## 📊 Project Overview

This project answers 52 analytical questions across 7 modules:

| Module | Questions Answered |
|---|---|
| Market Overview | Total market size, COVID impact, festive patterns |
| Segment Analysis | Best segment, top bikes, price distribution |
| EV vs Petrol Deep Dive | Market share growth, TCO, range comparison |
| Brand Analysis | Market leaders, brand coverage, price positioning |
| Specs & Performance | Power per rupee, mileage efficiency, value scores |
| AI Chatbot | Natural language Q&A over the dataset |
| Recommendation Engine | Personalised top 3 bike picks for any buyer |

---

## 🔑 Key Insights

- 🏆 **Hero MotoCorp** controls **32%** of India's two-wheeler market
- ⚡ **EV market share** grew from **~0% in 2019 to 10.6% in 2023**
- 💰 EVs cost just **Rs 0.2/km** vs Rs 1.6–3.5/km for petrol bikes
- 🛵 **Hero Splendor Plus** is India's undisputed sales king with 19M+ units
- 📍 **Maharashtra** leads EV adoption with 37K+ registrations
- 🔋 **Ultraviolette F77** has India's best EV range at 307km
- 🏁 **KTM** dominates the performance segment — top 3 most powerful bikes

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Data Generation | Python (pandas, numpy) |
| Storage | PostgreSQL |
| BI Dashboard | Power BI (DAX, Star Schema) |
| Web App | Streamlit |
| AI Features | Google Gemini API (gemini-1.5-flash) |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
india-bike-analysis/
│
├── data/
│   ├── raw/                    ← Original generated datasets
│   ├── clean/                  ← Cleaned CSVs
│   └── master/                 ← Merged master dataset
│       └── star_schema/        ← Dim + Fact tables
│
├── notebooks/
│   ├── 01_clean.ipynb          ← Data cleaning pipeline
│   ├── 02_merge.ipynb          ← Data merging + master creation
│   └── 03_star_schema.ipynb    ← Star schema generation
│
├── scripts/
│   └── load_to_postgres.py     ← PostgreSQL loader
│
├── streamlit_app/
│   ├── app.py                  ← Home page
│   ├── pages/
│   │   ├── 01_chatbot.py       ← AI Market Analyst chatbot
│   │   └── 02_recommend.py     ← Bike Recommender engine
│   └── utils/
│       ├── db.py               ← Database connection
│       ├── ai.py               ← Gemini API helpers
│       ├── theme.py            ← Shared CSS theme
│       └── sidebar.py          ← Shared sidebar component
│
├── powerbi/
│   └── india_bike_analysis.pbix ← Power BI report (5 pages)
│
├── requirements.txt
└── README.md
```

---

## 📈 Power BI Dashboard

The Power BI report has **5 pages**:

| Page | What it shows |
|---|---|
| **Market Overview** | Total sales trend, COVID impact, festive patterns, EV vs petrol |
| **EV vs Petrol** | Market share growth, TCO comparison, state adoption, top EVs |
| **Brand Analysis** | Market share, brand trends, price positioning, segment coverage |
| **Segment Analysis** | Segment breakdown, price distribution, growth trends |
| **Specs & Performance** | Power vs price, mileage efficiency, value score, cost per KM |

### Data Model — Star Schema

```
dim_bikes ──────────────────── fact_sales
    │                               │
    └── dim_brand          dim_date ┘
                               │
                          fact_ev_states

dim_bikes ──── fact_reviews
```

---

## 🤖 AI Features

### AI Market Analyst (Chatbot)
- Powered by **Google Gemini 1.5 Flash**
- Answers natural language questions about the dataset
- Topic-filtered suggested questions (7 categories)
- Typewriter effect response rendering
- Full conversation history

**Sample questions:**
```
"Which EV scooter has the best real-world range under Rs 1.5L?"
"Why is Hero MotoCorp still the market leader in 2023?"
"Is an EV actually cheaper than petrol over 5 years?"
```

### Bike Recommender
- User inputs budget, usage, fuel preference, priority, experience
- Gemini analyses all matching bikes and returns **top 3 picks**
- Each recommendation includes reasoning, strength, downside and verdict
- Live budget preview showing all matching options

---

## 🗃️ Dataset

The dataset was synthetically generated with realistic patterns based on India's actual two-wheeler market:

| File | Rows | Description |
|---|---|---|
| `bikes_master.csv` | 66 | All bikes with specs, pricing, ratings |
| `sales_monthly.csv` | 3,936 | Monthly sales 2019–2023 per bike |
| `ev_state_wise.csv` | 1,200 | State-wise EV registrations (20 states × 60 months) |
| `customer_reviews.csv` | 7,827 | Customer ratings with pros/cons |

**Realistic patterns included:**
- COVID sales crash (Apr–May 2020, Apr–May 2021)
- Festive season boost (Sep–Nov every year)
- EV exponential growth from 2021 onwards
- Maharashtra/Delhi/Karnataka leading EV adoption

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Power BI Desktop
- Google AI Studio API key

### Step 1 — Clone the repository
```bash
git clone https://github.com/yourusername/india-bike-analysis.git
cd india-bike-analysis
```

### Step 2 — Install dependencies
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

### Step 3 — Set up environment variables
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_api_key
DB_HOST=localhost
DB_NAME=india_bike_analysis
DB_USER=postgres
DB_PASSWORD=your_password
```

### Step 4 — Run the data pipeline
```bash
# Run notebooks in order
jupyter notebook notebooks/01_clean.ipynb
jupyter notebook notebooks/02_merge.ipynb

# Load to PostgreSQL
python scripts/load_to_postgres.py
```

### Step 5 — Run the Streamlit app
```bash
streamlit run streamlit_app/app.py
```

### Step 6 — Open Power BI
Open `powerbi/india_bike_analysis.pbix` in Power BI Desktop and refresh the data connection.

---

## 📦 Requirements

```
streamlit
pandas
numpy
psycopg2-binary
sqlalchemy
google-generativeai
python-dotenv
plotly
openpyxl
```

---

## 🎯 Skills Demonstrated

- **Python** — Data cleaning, merging, pipeline automation
- **SQL + PostgreSQL** — Star schema design, complex joins, indexing
- **Power BI** — 5-page dashboard, 20+ DAX measures, data modelling
- **Google Gemini API** — Context-aware chatbot, recommendation engine
- **Streamlit** — Full-stack web app with consistent theming
- **Data Modelling** — Proper star schema with dim/fact separation
- **End-to-end thinking** — Raw data → insights → deployed product

---

## 👤 About

**Om** | B.Tech CSE (AI & ML) | Oriental Institute of Science and Technology, Bhopal

- 📧 omjitpure11@gmail.com
- 💼 https://www.linkedin.com/in/om-jitpure-013424197/
- 🐙 https://github.com/omjit12/India-Two-Wheeler-Market-Analysis

---

## 📄 License

MIT License — feel free to use this project as a reference or template.
