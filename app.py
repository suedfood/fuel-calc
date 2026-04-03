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
    "SUV": {"Kia Sportage": 62, "Hyundai Tucson": 62, "Changan Oshan X7": 55, "MG HS": 55, "Haval H6": 58, "Haval Jolion": 55, "Kia Stonic": 45, "Cherry Tiggo 4 Pro": 51},
    "Pickup/4x4": {"Toyota Hilux/Revo": 80, "Isuzu D-Max": 76, "JAC T8": 76, "Toyota Fortuner": 80, "Land Cruiser": 93}
}

# 2. IMAGE MAPPING
cdn_base = "https://cdn.jsdelivr.net/gh/suedfood/fuel-calc@main/"

vehicle_images = {
    "CD 70": cdn_base + "CD70.png",
    "CG 125": cdn_base + "CG%20125.png",
    "GS 150": cdn_base + "GS%20150.png",
    "YBR 125": cdn_base + "YBR%20125.png",
    "Suzuki Alto": cdn_base + "Alto.png",
    "Suzuki Cultus": cdn_base + "Cultus.png",
    "Suzuki Wagon R": cdn_base + "Wagon%20R.png",
    "Suzuki Swift": cdn_base + "Swift.png",
    "Kia Picanto": cdn_base + "Picanto.png",
    "Suzuki Mehran": cdn_base + "Mehran.png",
    "Honda City": cdn_base + "Honda%20City.png",
    "Toyota Yaris": cdn_base + "Yaris.png",
    "Changan Alsvin": cdn_base + "Alswin.png",
    "Honda Civic": cdn_base + "Civic.png",
    "Toyota Corolla": cdn_base + "Corolla.png",
    "Hyundai Elantra": cdn_base + "Elantra.png",
    "Proton Saga": cdn_base + "Proton%20Saga.png",
    "Kia Sportage": cdn_base + "Sportage.png",
    "Hyundai Tucson": cdn_base + "Tucson.png",
    "Changan Oshan X7": cdn_base + "Oshan%20X7.png",
    "MG HS": cdn_base + "MG%20HS.png",
    "Haval H6": cdn_base + "Haval%20H6.png",
    "Haval Jolion": cdn_base + "Haval%20Jolion.png",
    "Kia Stonic": cdn_base + "Kia%20Stonic.png",
    "Cherry Tiggo 4 Pro": cdn_base + "Cherry%20Tiggo%20Pro%204.png",
    "Toyota Hilux/Revo": cdn_base + "Revo.png",
    "Isuzu D-Max": cdn_base + "ISUZU%20D-Max.png",
    "JAC T8": cdn_base + "Jac%20T-8.png",
    "Toyota Fortuner": cdn_base + "Fortuner.png",
    "Land Cruiser": cdn_base + "Land%20Cruiser.png"
}

# 3. UI SETUP
st.set_page_config(page_title="Fuel Surplus Calc", page_icon="⛽", layout="centered")

if 'step' not in st.session_state:
    st.session_state.step = 1

def move_to_next():
    st.session_state.step += 1

current_date = datetime.now().strftime("%B %d, %Y")

# 4. THE CSS (Zero-Font Diagnostic Version)
st.markdown(f"""
    <style>
    /* Strictly System Fonts to ensure instant Safari rendering */
    html, body, [class*="st-"], div, span, p, h1, h2, h3 {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        text-transform: none !important;
    }}

    /* Weights */
    h1, h3, [data-testid="stMetricValue"], .stAlert p {{ font-weight: 600 !important; }}
    label, p, .stCaption, [data-testid="stMetricLabel"] {{ font-weight: 400 !important; }}

    /* Layout & Scales */
    h1 {{ letter-spacing: -1px; font-size: 2.8rem !important; color: #1A1A1A; }}
    .subtitle {{ font-size: 1.15rem; color: #555; margin-top: -20px; margin-bottom: 30px; }}
    [data-testid="stImage"] img {{ width: 240px !important; height: 240px !important; object-fit: cover !important; border-radius: 12px !important; }}

    @media (max-width: 640px) {{
        h1 {{ font-size: 1.8rem !important; }}
        .subtitle {{ font-size: 1.0rem !important; margin-top: -10px !important; }}
        [data-testid="stImage"] img {{ width: 180px !important; height: 180px !important; }}
    }}
    
    .stAlert p {{ font-size: 1.15rem; line-height: 1.5; }}
    .custom-footer {{ font-size: 0.85rem; color: #AAA; margin-top: 4rem; padding-top: 1rem; border-top: 1px solid #EEE; }}
    </style>
    """, unsafe_allow_html=True)

# --- APP LAYOUT ---
st.title("⛽️ Pakistan Fuel Hike Impact")
st.markdown(f"### {current_date}")
st.markdown('<p class="subtitle">Find out how much more you’ll spend on fuel each month</p>', unsafe_allow_html=True)

# STEP 1
cat_choice = st.radio("Select vehicle category", list(categories.keys()), horizontal=True)
if st.session_state.step == 1:
    st.button("Continue", on_click=move_to_next)

# STEP 2
if st.session_state.step >= 2:
    model_choice = st.selectbox("Which vehicle do you drive?", list(categories[cat_choice].keys()))
    tank_size = categories[cat_choice][model_choice]
    
    img_url = vehicle_images.get(model_choice)
    if img_url:
        st.image(img_url, width=240)
    
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

# FINAL REPORT
if st.session_state.step >= 6:
    refill_volume_factor = 1 - (tank_scale / 10)
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
    st.markdown('<p class="custom-footer">Created by Syed Fahad Rizwan</p>', unsafe_allow_html=True)
