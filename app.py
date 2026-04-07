import streamlit as st
from datetime import datetime

# 1. THE DATA: Revised as of April 07, 2026
fuel_impacts = {
    "Petrol": {"hike": 56.83, "current": 378.00},
    "Diesel": {"hike": 184.49, "current": 520.35}
}

categories = {
    "Bike": {"CD 70": 9, "CG 125": 12, "GS 150": 12, "YBR 125": 13},
    "Hatchback": {"Suzuki Alto": 27, "Suzuki Cultus": 35, "Suzuki Wagon R": 35, "Suzuki Swift": 37, "Kia Picanto": 35, "Suzuki Mehran": 30},
    "Sedan": {"Honda City": 40, "Toyota Yaris": 42, "Changan Alsvin": 40, "Honda Civic": 47, "Toyota Corolla": 55, "Hyundai Elantra": 50, "Proton Saga": 40},
    "SUV": {"Kia Sportage": 62, "Hyundai Tucson": 62, "Changan Oshan X7": 55, "MG HS": 55, "Haval H6": 58, "Haval Jolion": 55, "Kia Stonic": 45, "Cherry Tiggo 4 Pro": 51},
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

if 'show_report' not in st.session_state:
    st.session_state.show_report = False

def trigger_report():
    st.session_state.show_report = True

def absolute_reset():
    st.session_state.clear()
    st.session_state.show_report = False

# 3. CSS FORCE FIELD: STRICT APPROVED WEIGHTS & TARGETED DROPDOWN FIX
st.markdown(f"""
    <style>
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

    /* Global Base: 500 Medium (Approved) */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], 
    [class*="st-"], div, span, p, h1, h2, h3 {{
        font-family: 'NeueHaas', -apple-system, sans-serif !important;
        text-transform: none !important;
        font-weight: 500 !important; 
        color: #31333F !important;
    }}
    
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        background-color: white !important;
    }}

    /* Specific Overrides: 400 Roman (Approved) */
    .subtitle {{
        font-weight: 400 !important;
        font-size: 1.15rem;
        color: #555 !important;
        margin-top: -20px;
        margin-bottom: 30px;
    }}

    div[role="radiogroup"] label p {{ font-weight: 400 !important; color: #31333F !important; opacity: 1 !important; }}
    div[data-baseweb="select"] div {{ font-weight: 400 !important; color: #31333F !important; }}
    [data-testid="stMetricLabel"] {{ letter-spacing: 0px; font-size: 15px !important; color: #555; font-weight: 400 !important; }}
    label, div[role="radiogroup"] label {{ font-size: 1rem !important; font-weight: 400 !important; }}
    .stCaption {{ color: #888; font-weight: 400 !important; }}
    
    .custom-footer {{
        font-family: 'NeueHaas' !important;
        font-weight: 400 !important;
        font-size: 0.85rem !important;
        color: #AAA !important;
        margin-top: 4rem;
        padding-top: 1rem;
        border-top: 1px solid #EEE;
    }}

    /* Headers & Metrics (500 Medium) */
    h1 {{ letter-spacing: -1.2px; font-size: 2.8rem !important; color: #1A1A1A !important; font-weight: 500 !important; }}
    h3, .stSubheader {{ letter-spacing: -0.5px; color: #444 !important; font-weight: 500 !important; }}
    [data-testid="stMetricValue"] {{ font-size: 42px !important; letter-spacing: -0.8px; color: #1A1A1A !important; font-weight: 500 !important; }}
    .stAlert p {{ font-size: 1.15rem; line-height: 1.5; font-weight: 500 !important; }}

    /* --- DARK MODE SELECTBOX & DROPDOWN FIX --- */
    div[data-baseweb="select"] > div {{
        background-color: #F0F2F6 !important;
        color: #31333F !important;
    }}
    
    /* Targets the floating listbox menu in dark mode */
    [data-baseweb="popover"] ul {{
        background-color: white !important;
    }}
    [data-baseweb="popover"] li {{
        background-color: white !important;
        color: #31333F !important;
        font-family: 'NeueHaas', sans-serif !important;
        font-weight: 400 !important;
    }}

    /* Button Styling */
    .stButton > button {{
        background-color: #1A1A1A !important;
        color: white !important;
        border-radius: 8px !important;
        width: 100% !important;
        font-weight: 500 !important;
        border: none !important;
        padding: 0.6rem !important;
    }}
    .stButton > button p {{ color: white !important; font-weight: 500 !important; }}

    /* RESET BUTTON ONLY (400 Roman Override) */
    .roman-btn button, .roman-btn button p {{
        font-weight: 400 !important;
    }}

    /* Image & UI Fixes */
    [data-testid="stImage"] img {{
        width: 240px !important;
        height: auto !important;
        mix-blend-mode: multiply;
        background-color: white !important;
        border-radius: 12px;
    }}
    [data-baseweb="slider"] {{ background-color: transparent !important; }}
    #MainMenu, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- APP CONTENT ---
st.title("⛽️ Pakistan Fuel Hike Impact")
st.markdown(f"### {datetime.now().strftime('%B %d, %Y')}")
st.markdown('<p class="subtitle">Find out how much more you’ll spend on fuel each month</p>', unsafe_allow_html=True)

# --- SEAMLESS AUTO-REVEAL FLOW ---
cat_choice = st.radio("Select vehicle category", list(categories.keys()), horizontal=True, index=None, key="cat_radio")

if cat_choice:
    model_choice = st.selectbox("Which vehicle do you drive?", list(categories[cat_choice].keys()), index=None, placeholder="Choose car...", key="model_select")
    
    if model_choice:
        tank_size = categories[cat_choice][model_choice]
        st.image(vehicle_images.get(model_choice, github_base + "CD70.png"))
        
        fuel_choice = st.selectbox("Fuel type", ["Petrol", "Diesel"], index=None, placeholder="Select fuel type...", key="fuel_select")
        
        if fuel_choice:
            fills = st.slider("How many times do you refuel each month?", 1, 10, 2, key="fills_slider")
            tank_scale = st.slider("On a scale of 1 to 10, how full is your tank when you refuel?", 1, 10, 2, key="tank_slider")
            
            if not st.session_state.show_report:
                st.button("Let's Go!", on_click=trigger_report)

# --- THE REPORT ---
if st.session_state.show_report:
    # Safety Check for valid inputs
    if all(st.session_state.get(k) is not None for k in ["cat_radio", "model_select", "fuel_select"]):
        refill_vol = 1 - (st.session_state.tank_slider / 10)
        current_tank = categories[st.session_state.cat_radio][st.session_state.model_select]
        per_tank = (current_tank * refill_vol) * fuel_impacts[st.session_state.fuel_select]["hike"]
        monthly = per_tank * st.session_state.fills_slider

        st.divider()
        st.subheader("Fuel Impact Report")
        c1, c2 = st.columns(2)
        c1.metric("Additional cost per tank", f"Rs. {per_tank:,.0f}")
        c2.metric("Total additional monthly cost", f"Rs. {monthly:,.0f}")
        
        st.error(f"To continue business as usual, you'll have to pay an additional Rs. {monthly:,.0f} per month")
        st.caption("Data reflects the April 2026 revised official pricing.")
        st.markdown('<p class="custom-footer">Created by Syed Fahad Rizwan</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="roman-btn">', unsafe_allow_html=True)
        st.button("Start Again", on_click=absolute_reset)
        st.markdown('</div>', unsafe_allow_html=True)
