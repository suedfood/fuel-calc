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

# Dynamic Date
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
    /* 500 - Medium (Using the filename from your upload) */
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

    html, body, [class*="st-"] {{
        font-family: 'NeueHaas', sans-serif;
        color: #1A1A1A;
    }}

    /* Title (Bold - 700) */
    h1 {{
        font-weight: 700 !important;
        letter-spacing: -1.2px;
        text-transform: uppercase;
        font-size: 2.8rem !important;
    }}

    /* Subheaders and Body (Roman - 400) */
    h3, p, span {{
        font-weight: 400 !important;
    }}

    /* Metric Values (Bold - 700) */
    [data-testid="stMetricValue"] {{
        font-weight: 700;
        font-size: 40px !important;
        letter-spacing: -0.5px;
    }}

    /* Metric Labels (Medium - 500) */
    [data-testid="stMetricLabel"] {{
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 13px !important;
        color: #555;
    }}
    
    /* Radio/Selectbox Labels (Medium - 500) */
    label {{
        font-weight: 500
