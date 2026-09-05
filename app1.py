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
# ATTRACTIVE DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(255,255,255,0.95),
            transparent 28%
        ),
        radial-gradient(
            circle at 95% 90%,
            rgba(191,219,254,0.65),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #eef5ff 0%,
            #f8f4ff 48%,
            #eefaf6 100%
        );
}


/* Main Title */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #172554;
    margin-top: 10px;
    margin-bottom: 5px;
}


/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #64748b;
    margin-bottom: 30px;
}


/* Section headings */
h2, h3 {
    color: #1e3a8a !important;
    font-weight: 750 !important;
}


/* Labels */
label {
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #334155 !important;
}


/* Select boxes and number inputs */
.stSelectbox > div > div,
.stNumberInput input {

    border-radius: 12px !important;
    border: 1px solid #cbd5e1 !important;

    min-height: 48px;

    font-size: 16px !important;

    background: rgba(255,255,255,0.90) !important;
}


/* Input Hover */
.stSelectbox > div > div:hover,
.stNumberInput input:hover {

    border-color: #6366f1 !important;
}


/* Predict Button */
.stButton > button {

    width: 100%;

    height: 58px;

    border-radius: 15px;

    border: none;

    font-size: 20px;

    font-weight: 750;

    color: white;

    background:
        linear-gradient(
            90deg,
            #4f46e5,
            #7c3aed
        );

    box-shadow:
        0 8px 20px rgba(79,70,229,0.25);

    transition: 0.3s;
}


/* Button Hover */
.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 12px 25px rgba(79,70,229,0.35);
}


/* Prediction Result */
[data-testid="stMetric"] {

    background: rgba(255,255,255,0.92);

    padding: 25px;

    border-radius: 18px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 8px 25px rgba(15,23,42,0.08);
}


/* Metric Label */
[data-testid="stMetricLabel"] {

    font-size: 17px !important;

}


/* Metric Value */
[data-testid="stMetricValue"] {

    font-size: 36px !important;

    font-weight: 800 !important;

}


/* Divider */
hr {

    border: none;

    height: 1px;

    background: #cbd5e1;

    margin: 25px 0;

}


/* Footer */
.footer {

    text-align: center;

    color: #64748b;

    font-size: 14px;

    margin-top: 35px;

}

</style>
""", unsafe_allow_html=True)


# TITLE


st.markdown(
    '<div class="main-title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)



# LOAD DATA AND MODEL

df = pd.read_csv("cleaned-home-data.csv")

with open("pipe.pkl", "rb") as file:
    model = pickle.load(file)


# =========================================================
# LOCATION DETAILS
# =========================================================

st.subheader("📍 Location Details")

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
        df[
            df["state"].astype(str) == selected_state
        ]["Location"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_location = st.selectbox(
        "Location",
        sorted(location_data)
    )


# =========================================================
# PROPERTY DETAILS
# =========================================================

st.divider()

st.subheader("🏡 Property Details")

col1, col2, col3 = st.columns(3)

with col1:

    carpet_area = st.number_input(
        "Carpet Area (sqft)",
        min_value=1.0,
        value=500.0,
        step=100.0
    )

    bhk = st.number_input(
        "BHK",
        min_value=1,
        value=2,
        step=1
    )

    bathroom = st.number_input(
        "Bathroom",
        min_value=1,
        value=2,
        step=1
    )


with col2:

    balcony = st.number_input(
        "Balcony",
        min_value=0,
        value=1,
        step=1
    )

    flat_floor = st.number_input(
        "Flat Floor",
        min_value=0,
        value=1,
        step=1
    )

    total_floors = st.number_input(
        "Total Floors",
        min_value=1,
        value=5,
        step=1
    )


with col3:

    parking_numbers = st.number_input(
        "Parking Numbers",
        min_value=0,
        value=1,
        step=1
    )

    parking_type = st.selectbox(
        "Parking Type",
        sorted(
            df["Parking Type"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )

    furnishing = st.selectbox(
        "Furnishing",
        sorted(
            df["Furnishing"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )


# =========================================================
# TRANSACTION DETAILS
# =========================================================

st.divider()

st.subheader("📋 Transaction Details")

transaction = st.selectbox(
    "Transaction Type",
    sorted(
        df["Transaction"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
)


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    "🔮 Predict House Price"
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_data = pd.DataFrame([{

        "state": selected_state,

        "Location": selected_location,

        "Carpet Area": carpet_area,

        "Transaction": transaction,

        "Furnishing": furnishing,

        "Bathroom": bathroom,

        "Balcony": balcony,

        "BHK": bhk,

        "FlatFloor": flat_floor,

        "TotalFloors": total_floors,

        "ParkingNumbers": parking_numbers,

        "Parking Type": parking_type

    }])


    prediction = model.predict(input_data)[0]


    # Prevent negative prediction
    if prediction < 0:
        prediction = 0.01


    # =====================================================
    # PRICE CONVERSION
    # =====================================================

    if prediction < 1:

        price_in_lakhs = prediction * 100

        price_text = (
            f"₹ {price_in_lakhs:.2f} Lakhs"
        )

    else:

        price_text = (
            f"₹ {prediction:.2f} Crores"
        )


    # =====================================================
    # RESULT
    # =====================================================

    st.divider()

    st.subheader("🏠 Estimated House Price")

    st.metric(
        label="Predicted Price",
        value=price_text
    )

    st.success(
        "✨ Estimated price based on the selected property details."
    )

    st.balloons()



    