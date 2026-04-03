import streamlit as st
from datetime import datetime

# 1. THE DATA
fuel_impacts = {
    "Petrol": {"hike": 137.24, "current": 458.41},
    "Diesel": {"hike": 184.49, "current": 520.35}
}

categories = {
    "Bike": {"CD 70": 9, "CG 125": 12, "GS 150": 12, "YBR 125": 13},
    "Hatchback": {"Suzuki Alto": 27, "Suzuki Cultus": 35, "Suzuki Wagon R": 35, "Suzuki Swift": 37, "Kia Picanto": 35, "Suzuki Mehran": 30},
    "Sedan": {"Honda City": 40, "Toyota Yaris": 42, "Changan Alsvin": 40, "Honda Civic": 47, "Toyota Corolla": 55, "Hyundai Elantra": 50, "Proton Saga": 40},
    "SUV/Crossover": {"Kia Sportage": 62, "Hyundai Tucson": 62, "Changan Oshan X7": 55, "MG HS": 55, "Haval H6": 58, "Haval Jolion": 55, "Kia Stonic": 45, "Cherry Tiggo 4 Pro": 51},
    "Pickup/4x4": {"Toyota Hilux/Revo": 80, "Isuzu D-Max": 76, "JAC T8": 76, "Toyota Fortuner": 80, "Land Cruiser": 93}
}

github_base = "https://raw.githubusercontent.com/suedfood/fuel-calc/main/"

vehicle_images = {
    "CD 70": github_base + "CD70.png", "CG 125": github_base + "CG%20125.png",
    "GS 150": github_base + "GS%20150.png", "YBR 125": github_base + "YBR%20125.png",
    "Suzuki Alto": github_base + "Alto.png", "Suzuki Cultus": github_base + "Cultus.png",
    "Suzuki Wagon R": github_base + "Wagon%20R.png", "Suzuki Swift": github_base + "Swift.png",
    "Kia Picanto": github_base + "Picanto.png", "Suzuki Mehran": github_base + "Mehran.png",
    "Honda City": github_base + "Honda%20City.png", "Toyota Yaris": github_base + "Yaris.png",
    "Changan Alsvin": github_base + "Alswin.png", "Honda Civic": github_base + "Civic.png",
    "Toyota Corolla": github_base + "Corolla.png", "Hyundai Elantra": github_base + "Elantra.png",
    "Proton Saga": github_base + "Proton%20Saga.png", "Kia Sportage": github_base + "Sportage.png",
    "Hyundai Tucson": github_base + "Tucson.png", "Changan Oshan X7": github_base + "Oshan%20X7.png",
    "MG HS": github_base + "MG%20HS.png", "Haval H6": github_base + "Haval%20H6.png",
    "Haval Jolion": github_base + "Haval%20Jolion.png", "Kia Stonic": github_base + "Kia%20Stonic.png",
    "Cherry Tiggo 4 Pro": github_base + "Cherry%20Tiggo%20Pro%204.png",
    "Toyota Hilux/Revo": github_base + "Revo.png", "Isuzu D-Max": github_base + "ISUZU%20D-Max.png",
    "JAC T8": github_base + "Jac%20T-8.png", "Toyota Fortuner": github_base + "Fortuner.png",
    "Land Cruiser": github_base + "Land%20Cruiser.png"
}

# 2. UI SETUP
st.set_page_config(page_title="Fuel Surplus Calc", page_icon="⛽", layout="centered")

if 'step' not in st.session_state:
    st.session_state.step = 1

def move_to_next():
    st.session_state.step += 1

# 3. THE CSS FORCE FIELD
# This targets Streamlit's base variables and forces them to Light Mode
st.markdown(f"""
    <style>
    /* 1. HIJACK THEME VARIABLES */
    :root {{
        --primary-color: #FF4B4B;
        --background-color: #FFFFFF;
        --secondary-background-color: #F0F2F6;
        --text-color: #31333F;
        --font: "NeueHaas", -apple-system, sans-serif;
    }}

    /* 2. FONT INJECTION */
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayRoman.ttf') format('truetype');
        font-weight: 400; font-display: swap;
    }}
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayMediu.ttf') format('truetype');
        font-weight: 500; font-display: swap;
    }}

    /* 3. HARD COLOR OVERRIDES for Dark Mode Browsers */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stToolbar"] {{
        background-color: #FFFFFF !important;
        color: #31333F !important;
    }}

    /* Force all text elements to dark gray */
    p, span, label, li, h1, h2, h3, h4, h5, h6, .stMarkdown, [data-testid="stMetricLabel"], [data-testid="stMetricValue"] {{
        color: #31333F !important;
        font-family: 'NeueHaas', -apple-system, sans-serif !important;
    }}

    /* Specific fix for Radio Button Labels (The glitch in your screenshot) */
    div[role="radiogroup"] label p {{
        color: #31333F !important;
        opacity: 1 !important;
    }}

    /* Subtitle Styling */
    .subtitle {{
        font-weight: 400 !important;
        font-size: clamp(1rem, 4vw, 1.15rem);
        color: #555 !important;
        margin-top: -20px;
        margin-bottom: 30px;
    }}

    /* Image responsive blending */
    [data-testid="stImage"] img {{
        max-width: 100% !important;
        height: auto !important;
        width: 240px !important;
        border-radius: 12px;
        mix-blend-mode: multiply;
        background-color: white !important;
    }}

    /* Slider & Button Parity */
    .stSlider {{ padding-top: 10px; }}
    .stButton>button {{ width: 100%; border-radius: 8px; }}

    /* Report Elements */
    [data-testid="stMetricValue"] {{ font-size: clamp(2rem, 8vw, 42px) !important; letter-spacing: -0.8px; }}
    
    /* Footer */
    .custom-footer {{
        font-family: 'NeueHaas' !important;
        font-weight: 400 !important;
        font-size: 0.85rem;
        color: #AAA !important;
        margin-top: 4rem;
        padding-top: 1rem;
        border-top: 1px solid #EEE;
    }}

    /* Hide the Streamlit clutter */
    #MainMenu, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- APP CONTENT ---
st.title("⛽️ Pakistan Fuel Hike Impact")
st.markdown(f"### {datetime.now().strftime('%B %d, %Y')}")
st.markdown('<p class="subtitle">Find out how much more you’ll spend on fuel each month</p>', unsafe_allow_html=True)

# PROGRESSIVE FLOW
# STEP 1
cat_choice = st.radio("Select vehicle category", list(categories.keys()), horizontal=True)
if st.session_state.step == 1:
    st.button("Continue", on_click=move_to_next)

# STEP 2
if st.session_state.step >= 2:
    model_choice = st.selectbox("Which vehicle do you drive?", list(categories[cat_choice].keys()))
    tank_size = categories[cat_choice][model_choice]
    
    img_url = vehicle_images.get(model_choice, github_base + "CD70.png")
    st.image(img_url)
    
    if st.session_state.step == 2:
        st.button("Continue", on_click=move_to_next)

# STEP 3
if st.session_state.step >= 3:
    fuel_choice = st.selectbox("Fuel type", ["Petrol", "Diesel"])
    if st.session_state.step == 3:
        st.button("Continue", on_click=move_to_next)

# STEP 4
if st.session_state.step >= 4:
    fills = st.slider("How many times do you refuel each month?", 1, 10, 2)
    if st.session_state.step == 4:
        st.button("Continue", on_click=move_to_next)

# STEP 5
if st.session_state.step >= 5:
    tank_scale = st.slider("On a scale of 1 to 10, how full is your tank when you refuel?", 1, 10, 2)
    if st.session_state.step == 5:
        st.button("Show Final Report", on_click=move_to_next)

# THE REPORT
if st.session_state.step >= 6:
    refill_vol = 1 - (tank_scale / 10)
    hike = fuel_impacts[fuel_choice]["hike"]
    per_tank = (tank_size * refill_vol) * hike
    monthly = per_tank * fills

    st.divider()
    st.subheader("Fuel Impact Report")
    c1, c2 = st.columns(2)
    c1.metric("Additional cost per tank", f"Rs. {per_tank:,.0f}")
    c2.metric("Total additional monthly cost", f"Rs. {monthly:,.0f}")
    
    st.error(f"To continue business as usual, you'll have to pay an additional Rs. {monthly:,.0f} per month")
    st.caption("Data reflects the April 3rd official price re-basing compared to March 2026.")
    st.markdown('<p class="custom-footer">Created by Syed Fahad Rizwan</p>', unsafe_allow_html=True)
