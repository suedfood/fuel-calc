import streamlit as st
from datetime import datetime

# 1. THE DATA (April 3, 2026)
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

# 2. UI SETUP & REFINED FONT INJECTION
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
    /* 700 - Bold */
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayBold.ttf') format('truetype');
        font-weight: 700;
    }}

    /* Apply font globally with higher specificity */
    html, body, [class*="st-"], div, span, p {{
        font-family: 'NeueHaas', -apple-system, sans-serif !important;
    }}

    /* Title Styling (Title Case, Bold 700) */
    h1 {{
        font-weight: 700 !important;
        letter-spacing: -1.2px;
        text-transform: none !important; /* Forces Title Case if typed that way */
        font-size: 2.8rem !important;
    }}

    /* Date and Subheaders (Roman 400) */
    h3 {{
        font-weight: 400 !important;
        letter-spacing: -0.5px;
        color: #333;
    }}

    /* Metrics Value (Bold 700) */
    [data-testid="stMetricValue"] {{
        font-weight: 700;
        font-size: 40px !important;
        letter-spacing: -0.8px;
    }}

    /* Metrics Labels (Medium 500, Title Case) */
    [data-testid="stMetricLabel"] {{
        font-weight: 500;
        text-transform: none !important;
        letter-spacing: 0px;
        font-size: 15px !important;
        color: #555;
    }}
    
    /* The Final Message Box - Reducing weight from 700 to 500 */
    .stAlert p {{
        font-weight: 500 !important;
        font-size: 1.1rem;
        line-height: 1.4;
    }}

    /* Removing uppercase from radio labels */
    div[role="radiogroup"] label {{
        text-transform: none !important;
        font-weight: 500 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("⛽ Pakistan Fuel Hike Impact")
st.markdown(f"### {current_date}")

# STEP 1: CATEGORY
cat_choice = st.radio("Select vehicle category", list(categories.keys()), horizontal=True)

# STEP 2: MODEL
model_choice = st.selectbox(f"Which vehicle do you drive?", list(categories[cat_choice].keys()))
tank_size = categories[cat_choice][model_choice]

# HALFTONE IMAGE PLACEHOLDER
st.image("https://via.placeholder.com/600x250.png?text=Halftone+Vehicle+Graphic", use_column_width=True)

# STEP 3: FUEL & USAGE
col1, col2 = st.columns(2)
with col1:
    fuel_choice = st.selectbox("Fuel type", ["Petrol", "Diesel"])
with col2:
    fills = st.slider("Fills per month", min_value=0.5, max_value=12.0, value=2.0, step=0.5)

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

# Final message with reduced weight (500) and no bolding markers to ensure CSS control
st.error(f"To continue business as usual, you'll have to pay an additional Rs. {monthly_total:,.0f} per month")

st.caption("Data reflects the April 3rd official price re-basing compared to March 2026.")
