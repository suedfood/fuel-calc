import streamlit as st
from datetime import datetime

# 1. THE DATA: Official Hike Data as of April 3, 2026
fuel_impacts = {
    "Petrol": {"hike": 137.24, "current": 458.41},
    "Diesel": {"hike": 184.49, "current": 520.35}
}

categories = {
    "Bikes": {"CD 70": 9, "CG 125": 12, "GS 150": 12, "YBR 125": 13},
    "Hatchbacks": {"Suzuki Alto": 27, "Suzuki Cultus": 35, "Suzuki Wagon R": 35, "Suzuki Swift": 37, "Kia Picanto": 35, "Suzuki Mehran": 30},
    "Sedans": {"Honda City": 40, "Toyota Yaris": 42, "Changan Alsvin": 40, "Honda Civic": 47, "Toyota Corolla": 55, "Hyundai Elantra": 50, "Proton Saga": 40},
    "SUVs/Crossovers": {"Kia Sportage": 62, "Hyundai Tucson": 62, "Changan Oshan X7": 55, "MG HS": 55, "Haval H6": 58, "Haval Jolion": 55, "Kia Stonic": 45, "Cherry Tiggo 4 Pro": 51},
    "Pickups/4x4s": {"Toyota Hilux/Revo": 80, "Isuzu D-Max": 76, "JAC T8": 76, "Toyota Fortuner": 80, "Land Cruiser": 93}
}

# 2. UI SETUP & FONT INJECTION
st.set_page_config(page_title="Fuel Surplus Calc", page_icon="⛽")

# Dynamic Date formatting
current_date = datetime.now().strftime("%B %d, %Y")

# GitHub Raw Base URL
github_base = "https://raw.githubusercontent.com/suedfood/fuel-calc/main/"

st.markdown(f"""
    <style>
    /* 400 - Roman */
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayRoman.ttf') format('truetype');
        font-weight: 400;
    }}
    /* 500 - Medium (Matching your 'Mediu' filename) */
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayMediu.ttf') format('truetype');
        font-weight: 500;
    }}

    /* Global Font Override */
    html, body, [class*="st-"], div, span, p {{
        font-family: 'NeueHaas', -apple-system, sans-serif !important;
        text-transform: none !important;
    }}

    /* ANCHOR POINTS - Medium (500) */
    /* Title, Metric Value, Subheaders, Date, and Alert */
    h1, h3, [data-testid="stMetricValue"], .stAlert p, .date-subheader {{
        font-weight: 500 !important;
        color: #1A1A1A;
    }}

    /* Title Scale */
    h1 {{
        letter-spacing: -1.2px;
        font-size: 2.8rem !important;
    }}

    /* Date Subheader - Restored to Medium */
    .date-subheader {{
        font-family: 'NeueHaas' !important;
        font-size: 1.2rem;
        color: #444;
        margin-bottom: 2rem;
        letter-spacing: -0.3px;
    }}

    /* Fuel Impact Report Header */
    h3 {{
        letter-spacing: -0.5px;
        font-size: 1.5rem !important;
    }}

    /* Metrics Value Scale */
    [data-testid="stMetricValue"] {{
        font-size: 42px !important;
        letter-spacing: -0.8px;
    }}

    /* INSTRUCTIONAL TEXT - Roman (400) */
    /* Labels, Radio Labels, Metric Labels, and Captions */
    label, div[role="radiogroup"] label, [data-testid="stMetricLabel"], .stCaption {{
        font-weight: 400 !important;
    }}

    /* Label Spacing and Color */
    [data-testid="stMetricLabel"] {{
        font-size: 15px !important;
        color: #666;
    }}

    label, div[role="radiogroup"] label {{
        font-size: 1rem !important;
        color: #333;
    }}

    /* Alert Box Polish */
    .stAlert p {{
        font-size: 1.15rem;
        line-height: 1.5;
    }}

    /* Captions */
    .stCaption {{
        color: #888;
        font-size: 0.9rem !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("⛽ Pakistan Fuel Hike Impact")
# Date is now Medium (500)
st.markdown(f'<p class="date-subheader">{current_date}</p>', unsafe_allow_html=True)

# --- SELECTION FLOW ---
cat_choice = st.radio("Select vehicle category", list(categories.keys()), horizontal=True)

model_choice = st.selectbox("Which vehicle do you drive?", list(categories[cat_choice].keys()))
tank_size = categories[cat_choice][model_choice]

# HALFTONE IMAGE PLACEHOLDER
st.image("https://via.placeholder.com/600x250.png?text=Halftone+Vehicle+Graphic", use_column_width=True)

col1, col2 = st.columns(2)
with col1:
    fuel_choice = st.selectbox("Fuel type", ["Petrol", "Diesel"])
with col2:
    fills = st.slider("How many times do you refuel each month?", min_value=0.5, max_value=12.0, value=2.0, step=0.5)

# --- CALCULATIONS ---
hike = fuel_impacts[fuel_choice]["hike"]
per_tank = tank_size * hike
monthly_total = per_tank * fills

# --- THE REPORT ---
st.divider()
st.subheader("Fuel Impact Report")

c1, c2 = st.columns(2)
c1.metric("Additional cost per tank", f"Rs. {per_tank:,.0f}")
c2.metric("Total additional monthly cost", f"Rs. {monthly_total:,.0f}")

# Final Bottom Line Message (Medium 500)
st.error(f"To continue business as usual, you'll have to pay an additional Rs. {monthly_total:,.0f} per month")

st.caption("Data reflects the April 3rd official price re-basing compared to March 2026.")
