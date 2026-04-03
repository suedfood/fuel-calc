import streamlit as st

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

# 2. UI SETUP
st.set_page_config(page_title="Fuel Surplus Calc", page_icon="⛽")

st.title("⛽ Pakistan Fuel Impact Analysis")
st.markdown("### April 3, 2026 War-Time Price Re-basing")

# STEP 1: CATEGORY (Horizontal Radio)
cat_choice = st.radio("Select Vehicle Category", list(categories.keys()), horizontal=True)

# STEP 2: MODEL (Dropdown)
model_choice = st.selectbox(f"Which {cat_choice} do you drive?", list(categories[cat_choice].keys()))
tank_size = categories[cat_choice][model_choice]

# AESTHETIC TOUCH: Placeholder for your halftone photo
# You can replace this URL with your actual halftone designs
st.image("https://via.placeholder.com/600x200.png?text=Halftone+Vehicle+Graphic", use_column_width=True)

# STEP 3: FUEL & USAGE
col1, col2 = st.columns(2)
with col1:
    fuel_choice = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
with col2:
    # Cute slider with 0.5 increments
    fills = st.slider("Fills per month", min_value=0.5, max_value=12.0, value=2.0, step=0.5)

# 3. THE CALCULATION
hike = fuel_impacts[fuel_choice]["hike"]
per_tank = tank_size * hike
monthly_total = per_tank * fills

# 4. THE REPORT
st.divider()
st.subheader("Fuel Impact Report")

c1, c2 = st.columns(2)
c1.metric("Additional Cost / Tank", f"Rs. {per_tank:,.0f}")
c2.metric("Total Additional Monthly Cost", f"Rs. {monthly_total:,.0f}")

st.error(f"**TO CONTINUE BUSINESS AS USUAL, YOU'LL HAVE TO PAY AN ADDITIONAL RS. {monthly_total:,.0f} PER MONTH**")

st.caption("Data reflects the April 3rd official price re-basing compared to Ramadan 2026.")
