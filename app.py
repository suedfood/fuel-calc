import streamlit as st
from datetime import datetime

# 1. THE DATA: Official Hike Data as of April 3, 2026
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
    "JAC T8": github_base + "Jac%20T-8.png",
    "Toyota Fortuner": github_base + "Fortuner.png",
    "Land Cruiser": github_base + "Land%20Cruiser.png"
}

# 3. UI SETUP & FONT INJECTION
st.set_page_config(page_title="Fuel Surplus Calc", page_icon="⛽", layout="centered")

# Initialize State for the Final Reveal
if 'show_report' not in st.session_state:
    st.session_state.show_report = False

def trigger_report():
    st.session_state.show_report = True

current_date = datetime.now().strftime("%B %d, %Y")

st.markdown(f"""
    <style>
    /* 1. DARK MODE KILLER & THEME LOCK */
    :root {{
        --primary-color: #FF4B4B;
        --background-color: #FFFFFF;
        --secondary-background-color: #F0F2F6;
        --text-color: #31333F;
    }}

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        background-color: white !important;
        color: #31333F !important;
    }}

    /* 2. FONT INJECTION - NEUE HAAS FOR MOBILE & DESKTOP */
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayRoman.ttf') format('truetype');
        font-weight: 400;
        font-display: swap;
    }}
    @font-face {{
        font-family: 'NeueHaas';
        src: url('{github_base}NeueHaasDisplayMediu.ttf') format('truetype');
        font-weight: 500;
        font-display: swap;
    }}

    /* Global Typography Reset */
    html, body, [class*="st-"], div, span, p, h1, h2, h3 {{
        font-family: 'NeueHaas', -apple-system, sans-serif !important;
        text-transform: none !important;
    }}

    h1 {{ 
        letter-spacing: -1.2px; 
        font-size: clamp(2rem, 8vw, 2.8rem) !important; 
        color: #1A1A1A; 
        font-weight: 500 !important; 
    }}
    
    h3, .stSubheader {{ 
        letter-spacing: -0.5px; 
        color: #444; 
        font-weight: 500 !important; 
    }}

    .subtitle {{
        font-weight: 400 !important;
        font-size: clamp(1rem, 4vw, 1.15rem);
        color: #555 !important;
        margin-top: -20px;
        margin-bottom: 30px;
    }}

    /* 3. IMAGE BLENDING & RESPONSIVE BOX */
    [data-testid="stImage"] img {{
        max-width: 100% !important;
        height: auto !important;
        width: 240px !important;
        border-radius: 12px !important;
        margin-top: -5px;
        margin-bottom: 25px;
        background-color: white !important;
        mix-blend-mode: multiply;
    }}

    /* 4. METRICS: MEDIUM WEIGHT (500) LOCK */
    [data-testid="stMetricValue"] {{ 
        font-size: clamp(2rem, 10vw, 42px) !important; 
        letter-spacing: -0.8px; 
        color: #1A1A1A !important;
        font-weight: 500 !important;
    }}
    [data-testid="stMetricLabel"] {{ font-size: 15px !important; color: #555; font-weight: 400 !important; }}

    /* 5. BUTTON HARDENING - LET'S GO! */
    .stButton > button {{
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        width: 100% !important;
        font-weight: 500 !important;
        opacity: 1 !important;
        margin-top: 20px;
    }}
    .stButton > button:hover {{ background-color: #444444 !important; }}
    .stButton > button p {{ color: white !important; font-weight: 500 !important; }}

    /* Fix Radio/Select text in Dark Mode */
    div[role="radiogroup"] label p {{ color: #31333F !important; opacity: 1 !important; }}
    label, p, span {{ font-weight: 400 !important; }}
    .stCaption {{ color: #888; font-weight: 400 !important; }}
    
    .custom-footer {{
        font-weight: 400 !important;
        font-size: 0.85rem !important;
        color: #AAA !important;
        margin-top: 4rem;
        padding-top: 1rem;
        border-top: 1px solid #EEE;
    }}

    /* Hide Streamlit Clutter */
    #MainMenu, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("⛽️ Pakistan Fuel Hike Impact")
st.markdown(f"### {current_date}")
st.markdown('<p class="subtitle">Find out how much more you’ll spend on fuel each month</p>', unsafe_allow_html=True)

# --- SEAMLESS AUTO-REVEAL FLOW ---
# Using index=None to ensure nothing is pre-selected and "dead"

# STEP 1: CATEGORY
cat_choice = st.radio("Select vehicle category", list(categories.keys()), horizontal=True, index=None)

if cat_choice:
    # STEP 2: MODEL
    model_choice = st.selectbox("Which vehicle do you drive?", list(categories[cat_choice].keys()), index=None, placeholder="Choose your car...")
    
    if model_choice:
        tank_size = categories[cat_choice][model_choice]
        img_url = vehicle_images.get(model_choice, github_base + "CD70.png")
        st.image(img_url)
        
        # STEP 3: FUEL
        fuel_choice = st.selectbox("Fuel type", ["Petrol", "Diesel"], index=None, placeholder="Select fuel type...")
        
        if fuel_choice:
            # STEP 4: FREQUENCY
            fills = st.slider("How many times do you refuel each month?", 1, 10, 2)
            
            # STEP 5: TANK SCALE
            tank_scale = st.slider("On average, how full is your tank when you refuel?", 1, 10, 2)
            
            # THE ACTION BUTTON
            st.button("Let's Go!", on_click=trigger_report)

# --- THE FINAL REPORT ---
if st.session_state.show_report:
    try:
        refill_vol = 1 - (tank_scale / 10)
        hike = fuel_impacts[fuel_choice]["hike"]
        per_tank = (tank_size * refill_vol) * hike
        monthly_total = per_tank * fills

        st.divider()
        st.subheader("Fuel Impact Report")
        
        c1, c2 = st.columns(2)
        c1.metric("Additional cost per tank", f"Rs. {per_tank:,.0f}")
        c2.metric("Total additional monthly cost", f"Rs. {monthly_total:,.0f}")
        
        st.error(f"To continue business as usual, you'll have to pay an additional Rs. {monthly_total:,.0f} per month")
        st.caption("Data reflects the April 3rd official price re-basing compared to March 2026.")
        st.markdown('<p class="custom-footer">Created by Syed Fahad Rizwan</p>', unsafe_allow_html=True)
        
        if st.button("Start Over"):
            st.session_state.show_report = False
            st.rerun()
    except NameError:
        # Fallback if a user somehow triggers report without selecting everything
        st.warning("Please complete all steps above first.")
