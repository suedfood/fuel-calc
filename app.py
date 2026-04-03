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

# 2. COMPLETE IMAGE MAPPING INFRASTRUCTURE
# Paste your custom image URLs between the quotes for each vehicle below.
vehicle_images = {
    # Bikes
    "CD 70": "https://placehold.co/600x400",
    "CG 125": "",
    "GS 150": "",
    "YBR 125": "",
    # Hatchbacks
    "Suzuki Alto": "",
    "Suzuki Cultus": "",
    "Suzuki Wagon R": "",
    "Suzuki Swift": "",
    "Kia Picanto": "",
    "Suzuki Mehran": "",
    # Sedans
    "Honda City": "",
    "Toyota Yaris": "",
    "Changan Alsvin": "",
    "Honda Civic": "",
    "Toyota Corolla": "",
    "Hyundai Elantra": "",
    "Proton Saga": "",
    # SUVs/Crossovers
    "Kia Sportage": "",
    "Hyundai Tucson": "",
    "Changan Oshan X7": "",
    "MG HS": "",
    "Haval H6": "",
    "Haval Jolion": "",
    "Kia Stonic": "",
    "Cherry Tiggo 4 Pro": "",
    # Pickups/4x4s
    "Toyota Hilux/Revo": "",
    "Isuzu D-Max": "",
    "JAC T8": "",
    "Toyota Fortuner": "",
    "Land Cruiser": ""
}

# 3. UI SETUP & FONT INJECTION
st.set_page_config(page_title="Fuel Surplus Calc", page_icon="⛽")

if 'step' not in st.session_state:
    st.session_state.step = 1

def move_to_next():
    st.session_state.step += 1

current_date = datetime.now().strftime("%B %d, %Y")
github_base = "https://raw.githubusercontent.com/suedfood/fuel-calc/main/"

st.markdown(f"""
    <style>
    /* 400 - Roman */
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayRoman.ttf') format('truetype');
        font-weight: 400;
    }}
    /* 500 - Medium */
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayMediu.ttf') format('truetype');
        font-weight: 500;
    }}

    /* Global Font Override - Strictly Neue Haas Medium */
    html, body, [class*="st-"], div, span, p, h1, h2, h3 {{
        font-family: 'NeueHaas', -apple-system, sans-serif !important;
        text-transform: none !important;
        font-weight: 500 !important; 
    }}

    /* SURGICAL WEIGHT REDUCTION (To Roman 400) */
    div[role="radiogroup"] label p {{ font-weight: 400 !important; }}
    div[data-baseweb="select"] div {{ font-weight: 400 !important; }}

    /* Title Styling */
    h1 {{
        letter-spacing: -1.2px;
        font-size: 2.8rem !important;
        color: #1A1A1A;
    }}

    /* Dynamic Date & Subheaders */
    h3 {{
        letter-spacing: -0.5px;
        color: #444;
    }}

    /* The Numbers */
    [data-testid="stMetricValue"] {{
        font-size: 42px !important;
        letter-spacing: -0.8px;
        color: #1A1A1A;
    }}

    /* Metric Labels */
    [data-testid="stMetricLabel"] {{
        letter-spacing: 0px;
        font-size: 15px !important;
        color: #555;
        font-weight: 400 !important;
    }}
    
    /* The Final Message Box */
    .stAlert p {{
        font-size: 1.15rem;
        line-height: 1.5;
        font-weight: 500 !important;
    }}

    /* Input Labels and Radio Labels */
    label, div[role="radiogroup"] label {{
        font-size: 1rem !important;
        font-weight: 400 !important;
    }}

    /* Captions */
    .stCaption {{
        color: #888;
        font-weight: 400 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("⛽️ Pakistan Fuel Hike Impact")
st.markdown(f"### {current_date}")

# --- PROGRESSIVE FLOW ---

# STEP 1: CATEGORY
cat_choice = st.radio("Select vehicle category", list(categories.keys()), horizontal=True)
if st.session_state.step == 1:
    st.button("Continue", on_click=move_to_next)

# STEP 2: MODEL & DYNAMIC IMAGE
if st.session_state.step >= 2:
    model_choice = st.selectbox("Which vehicle do you drive?", list(categories[cat_choice].keys()))
    tank_size = categories[cat_choice][model_choice]
    
    # Logic: Look up image or use default halftone if link is missing
    img_url = vehicle_images.get(model_choice, "")
    selected_img = img_url if img_url else "https://via.placeholder.com/600x250.png?text=Halftone+Vehicle+Graphic"
    st.image(selected_img, use_column_width=True)
    
    if st.session_state.step == 2:
        st.button("Continue", on_click=move_to_next)

# STEP 3: FUEL
if st.session_state.step >= 3:
    fuel_choice = st.selectbox("Fuel type", ["Petrol", "Diesel"])
    if st.session_state.step == 3:
        st.button("Continue", on_click=move_to_next)

# STEP 4: REFUEL FREQUENCY
if st.session_state.step >= 4:
    fills = st.slider("How many times do you refuel each month?", min_value=0.5, max_value=12.0, value=2.0, step=0.5)
    if st.session_state.step == 4:
        st.button("Continue", on_click=move_to_next)

# STEP 5: TANK FULLNESS
if st.session_state.step >= 5:
    tank_fullness = st.slider("On average, how full is your vehicle's tank when you refuel?", min_value=0, max_value=100, value=0, step=5, format="%d%%")
    if st.session_state.step == 5:
        st.button("Show Final Report", on_click=move_to_next)

# --- THE REPORT ---
if st.session_state.step >= 6:
    refill_volume_factor = 1 - (tank_fullness / 100)
    hike = fuel_impacts[fuel_choice]["hike"]
    per_tank = (tank_size * refill_volume_factor) * hike
    monthly_total = per_tank * fills

    st.divider()
    st.subheader("Fuel Impact Report")
    c1, c2 = st.columns(2)
    c1.metric("Additional cost per tank", f"Rs. {per_tank:,.0f}")
    c2.metric("Total additional monthly cost", f"Rs. {monthly_total:,.0f}")
    st.error(f"To continue business as usual, you'll have to pay an additional Rs. {monthly_total:,.0f} per month")
    st.caption("Data reflects the April 3rd official price re-basing compared to March 2026.")
