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

# 2. IMAGE MAPPING: Synced with your GitHub Filenames
github_base = "https://raw.githubusercontent.com/suedfood/fuel-calc/main/"

vehicle_images = {
    "CD 70": github_base + "CD70.png",
    "CG 125": github_base + "CG%20125.png",
    "GS 150": github_base + "GS%20150.png",
    "YBR 125": github_base + "YBR%20125.png",
    "Suzuki Alto": github_base + "Alto.png",
    "Suzuki Cultus": github_base + "Cultus.png",
    "Suzuki Wagon R": github_base + "Wagon%20R.png",
    "Suzuki Swift": github_base + "Swift.png",
    "Kia Picanto": github_base + "Picanto.png",
    "Suzuki Mehran": github_base + "Mehran.png",
    "Honda City": github_base + "Honda%20City.png",
    "Toyota Yaris": github_base + "Yaris.png",
    "Changan Alsvin": github_base + "Alswin.png",
    "Honda Civic": github_base + "Civic.png",
    "Toyota Corolla": github_base + "Corolla.png",
    "Hyundai Elantra": github_base + "Elantra.png",
    "Proton Saga": github_base + "Proton%20Saga.png",
    "Kia Sportage": github_base + "Sportage.png",
    "Hyundai Tucson": github_base + "Tucson.png",
    "Changan Oshan X7": github_base + "Oshan%20X7.png",
    "MG HS": github_base + "MG%20HS.png",
    "Haval H6": github_base + "Haval%20H6.png",
    "Haval Jolion": github_base + "Haval%20Jolion.png",
    "Kia Stonic": github_base + "Kia%20Stonic.png",
    "Cherry Tiggo 4 Pro": github_base + "Cherry%20Tiggo%20Pro%204.png",
    "Toyota Hilux/Revo": github_base + "Revo.png",
    "Isuzu D-Max": github_base + "ISUZU%20D-Max.png",
    "Jac T-8": github_base + "Jac%20T-8.png",
    "Toyota Fortuner": github_base + "Fortuner.png",
    "Land Cruiser": github_base + "Land%20Cruiser.png"
}

# 3. UI SETUP & FONT INJECTION
st.set_page_config(page_title="Fuel Surplus Calc", page_icon="⛽")

if 'step' not in st.session_state:
    st.session_state.step = 1

def move_to_next():
    st.session_state.step += 1

current_date = datetime.now().strftime("%B %d, %Y")

st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayRoman.ttf') format('truetype');
        font-weight: 400;
    }}
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayMediu.ttf') format('truetype');
        font-weight: 500;
    }}

    html, body, [class*="st-"], div, span, p, h1, h2, h3 {{
        font-family: 'NeueHaas', -apple-system, sans-serif !important;
        text-transform: none !important;
        font-weight: 500 !important; 
    }}

    [data-testid="stImage"] img {{
        width: 240px !important;
        height: 240px !important;
        object-fit: cover !important;
        border-radius: 12px !important;
        margin-top: -5px;
        margin-bottom: 25px;
    }}

    div[role="radiogroup"] label p {{ font-weight: 400 !important; }}
    div[data-baseweb="select"] div {{ font-weight: 400 !important; }}
    h1 {{ letter-spacing: -1.2px; font-size: 2.8rem !important; color: #1A1A1A; }}
    h3 {{ letter-spacing: -0.5px; color: #444; }}
    [data-testid="stMetricValue"] {{ font-size: 42px !important; letter-spacing: -0.8px; color: #1A1A1A; }}
    [data-testid="stMetricLabel"] {{ letter-spacing: 0px; font-size: 15px !important; color: #555; font-weight: 400 !important; }}
    .stAlert p {{ font-size: 1.15rem; line-height: 1.5; font-weight: 500 !important; }}
    label, div[role="radiogroup"] label {{ font-size: 1rem !important; font-weight: 400 !important; }}
    .stCaption {{ color: #888; font-weight: 400 !important; }}

    /* Classy Footer Styling */
    .footer {{
        font-weight: 400 !important;
        font-size: 0.8rem;
        color: #AAA;
        text-align: left;
        margin-top: 4rem;
        border-top: 1px solid #EEE;
        padding-top: 1rem;
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

# STEP 2: MODEL & IMAGE
if st.session_state.step >= 2:
    model_choice = st.selectbox("Which vehicle do you drive?", list(categories[cat_choice].keys()))
    tank_size = categories[cat_choice][model_choice]
    
    img_url = vehicle_images.get(model_choice, "")
    selected_img = img_url if img_url else "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=400&h=400"
    st.image(selected_img, width=240)
    
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

# --- FOOTER ---
st.markdown('<p class="footer">Created by Syed Fahad Rizwan</p>', unsafe_allow_html=True)
