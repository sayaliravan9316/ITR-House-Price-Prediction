import streamlit as st
import pandas as pd
import pickle

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# =========================================================
# CUSTOM DESIGN / CSS
# =========================================================

st.markdown("""
<style>

/* ===============================
   MAIN BACKGROUND
   =============================== */

.stApp {
    background: linear-gradient(
        135deg,
        #f6f1e9 0%,
        #e8f0e8 45%,
        #dce8f5 100%
    );
}


/* ===============================
   MAIN CONTENT
   =============================== */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}


/* ===============================
   MAIN TITLE
   =============================== */

.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    margin-bottom: 8px;
    letter-spacing: 1px;
}


/* ===============================
   SUBTITLE
   =============================== */

.subtitle {
    text-align: center;
    font-size: 21px;
    font-weight: 500;
    margin-bottom: 35px;
}


/* ===============================
   SECTION HEADINGS
   =============================== */

h1 {
    font-size: 36px !important;
    font-weight: 800 !important;
}

h2 {
    font-size: 30px !important;
    font-weight: 800 !important;
}

h3 {
    font-size: 25px !important;
    font-weight: 750 !important;
}


/* ===============================
   LABELS
   =============================== */

label {
    font-size: 18px !important;
    font-weight: 700 !important;
}


/* ===============================
   INPUT BOXES
   =============================== */

.stSelectbox > div > div,
.stNumberInput > div > div {
    min-height: 50px;
    border-radius: 12px;
    font-size: 17px;
}


/* Input text */

.stSelectbox div,
.stNumberInput input {
    font-size: 17px !important;
}


/* ===============================
   BUTTON
   =============================== */

.stButton > button {
    width: 100%;
    height: 62px;
    border-radius: 15px;
    font-size: 23px !important;
    font-weight: 800 !important;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
}


/* ===============================
   PREDICTION METRIC
   =============================== */

[data-testid="stMetric"] {
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(0,0,0,0.08);
    background: rgba(255,255,255,0.75);
}


/* Metric label */

[data-testid="stMetricLabel"] {
    font-size: 20px !important;
    font-weight: 700 !important;
}


/* Metric value */

[data-testid="stMetricValue"] {
    font-size: 44px !important;
    font-weight: 900 !important;
}


/* ===============================
   SUCCESS MESSAGE
   =============================== */

.stAlert {
    font-size: 17px !important;
    border-radius: 12px;
}


/* ===============================
   DIVIDER
   =============================== */

hr {
    margin-top: 25px;
    margin-bottom: 25px;
}


/* ===============================
   FOOTER
   =============================== */

.footer {
    text-align: center;
    font-size: 16px;
    font-weight: 600;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict the estimated price of a house using property details</div>',
    unsafe_allow_html=True
)


# =========================================================
# LOAD DATASET
# =========================================================

try:

    df = pd.read_csv("cleaned-home-data.csv")

except FileNotFoundError:

    st.error("❌ cleaned-home-data.csv file not found.")
    st.stop()


# =========================================================
# LOAD MODEL
# =========================================================

try:

    with open("pipe.pkl", "rb") as file:
        model = pickle.load(file)

except FileNotFoundError:

    st.error("❌ pipe.pkl file not found.")
    st.stop()


# =========================================================
# LOCATION DETAILS
# =========================================================

st.header("📍 Location Details")

col1, col2 = st.columns(2)

with col1:

    states = sorted(
        df["state"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_state = st.selectbox(
        "State",
        states
    )


with col2:

    location_data = (
        df[df["state"].astype(str) == selected_state]["Location"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    location_data = sorted(location_data)

    selected_location = st.selectbox(
        "Location",
        location_data
    )


# =========================================================
# PROPERTY DETAILS
# =========================================================

st.header("🏡 Property Details")

col1, col2, col3 = st.columns(3)

with col1:

    carpet_area = st.number_input(
        "Carpet Area (sqft)",
        min_value=1.0,
        value=500.0,
        step=10.0
    )


with col2:

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=20,
        value=2,
        step=1
    )


with col3:

    bathroom = st.number_input(
        "Bathroom",
        min_value=1,
        max_value=20,
        value=2,
        step=1
    )


col1, col2, col3 = st.columns(3)

with col1:

    balcony = st.number_input(
        "Balcony",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )


with col2:

    flat_floor = st.number_input(
        "Flat Floor",
        min_value=0,
        max_value=100,
        value=1,
        step=1
    )


with col3:

    total_floors = st.number_input(
        "Total Floors",
        min_value=1,
        max_value=100,
        value=5,
        step=1
    )


# =========================================================
# ADDITIONAL DETAILS
# =========================================================

st.header("🔑 Additional Details")

col1, col2, col3 = st.columns(3)

with col1:

    parking_numbers = st.number_input(
        "Parking Numbers",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )


with col2:

    parking_types = sorted(
        df["Parking Type"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_parking = st.selectbox(
        "Parking Type",
        parking_types
    )


with col3:

    furnishing_types = sorted(
        df["Furnishing"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_furnishing = st.selectbox(
        "Furnishing",
        furnishing_types
    )


col1, col2 = st.columns(2)

with col1:

    transaction_types = sorted(
        df["Transaction"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_transaction = st.selectbox(
        "Transaction Type",
        transaction_types
    )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.write("")

predict_button = st.button(
    "🔮  Predict House Price"
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_data = pd.DataFrame([{

        "state": selected_state,

        "Location": selected_location,

        "Carpet Area": carpet_area,

        "Transaction": selected_transaction,

        "Furnishing": selected_furnishing,

        "Bathroom": bathroom,

        "Balcony": balcony,

        "BHK": bhk,

        "FlatFloor": flat_floor,

        "TotalFloors": total_floors,

        "ParkingNumbers": parking_numbers,

        "Parking Type": selected_parking

    }])


    try:

        # Predict price

        prediction = model.predict(input_data)[0]


        # Prevent negative prediction

        if prediction < 0:

            prediction = 0.01


        # =================================================
        # CONVERT PRICE
        # =================================================

        if prediction < 1:

            price_in_lakhs = prediction * 100

            price_text = f"₹ {price_in_lakhs:.2f} Lakhs"

        else:

            price_text = f"₹ {prediction:.2f} Crores"


        # =================================================
        # RESULT
        # =================================================

        st.divider()

        st.subheader("🏠 Estimated House Price")

        st.metric(
            label="Predicted Price",
            value=price_text
        )

        st.success(
            "✅ Estimated price based on the selected property details."
        )

        # Celebration

        st.balloons()


    except Exception as e:

        st.error(
            f"❌ Prediction Error: {e}"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="footer">🏠 House Price Prediction | Machine Learning Project</div>',
    unsafe_allow_html=True
)