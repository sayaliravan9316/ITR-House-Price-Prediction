
import streamlit as st
import pandas as pd
import pickle


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# =========================================================
# SIMPLE PROFESSIONAL UI
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f8fafc;
}

.block-container {
    max-width: 1150px;
    padding-top: 30px;
    padding-bottom: 40px;
}


/* ---------------- HEADER ---------------- */

.title {
    text-align: center;
    color: #1f4e79;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666666;
    font-size: 16px;
    margin-bottom: 35px;
}


/* ---------------- SECTION ---------------- */

.section-title {
    color: #1f4e79;
    font-size: 22px;
    font-weight: 650;
    padding-bottom: 7px;
    border-bottom: 2px solid #1f4e79;
    margin-top: 25px;
    margin-bottom: 20px;
}


/* ---------------- INPUT LABEL ---------------- */

label {
    font-weight: 600 !important;
    color: #333333 !important;
}


/* ---------------- INPUT BOX ---------------- */

div[data-baseweb="select"] > div {
    border-radius: 6px;
}

div[data-testid="stNumberInput"] input {
    border-radius: 6px;
}


/* ---------------- BUTTON ---------------- */

.stButton > button {
    background-color: #1f4e79;
    color: white;
    border-radius: 7px;
    height: 50px;
    font-size: 17px;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background-color: #163a5f;
    color: white;
}


/* ---------------- RESULT ---------------- */

.result-container {
    background-color: white;
    border: 2px solid #1f4e79;
    border-radius: 12px;
    padding: 25px;
    margin-top: 30px;
    text-align: center;
}

.result-title {
    color: #555555;
    font-size: 18px;
    font-weight: 600;
}

.result-price {
    color: #1f4e79;
    font-size: 36px;
    font-weight: 700;
    margin-top: 8px;
}

.result-text {
    color: #777777;
    font-size: 14px;
    margin-top: 5px;
}


/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;
    color: #777777;
    font-size: 13px;
    margin-top: 40px;
    padding-top: 15px;
    border-top: 1px solid #dddddd;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("cleaned-home-data.csv")


# =========================================================
# LOAD MODEL
# =========================================================

with open("pipe.pkl", "rb") as file:
    model = pickle.load(file)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based House Price Estimation System'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# LOCATION DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">📍 Location Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    states = sorted(
        df["state"].dropna().unique()
    )

    selected_state = st.selectbox(
        "Select State",
        states
    )


with col2:

    locations = sorted(
        df.loc[
            df["state"] == selected_state,
            "Location"
        ]
        .dropna()
        .unique()
    )

    selected_location = st.selectbox(
        "Select Location",
        locations
    )


# =========================================================
# PROPERTY DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">🏠 Property Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    carpet_area = st.number_input(
        "Carpet Area (sqft)",
        min_value=0,
        value=500,
        step=100
    )


with col2:

    bhk = st.selectbox(
        "BHK",
        sorted(
            df["BHK"]
            .dropna()
            .unique()
        )
    )


with col3:

    bathroom = st.selectbox(
        "Bathroom",
        sorted(
            df["Bathroom"]
            .dropna()
            .unique()
        )
    )


with col4:

    balcony = st.selectbox(
        "Balcony",
        sorted(
            df["Balcony"]
            .dropna()
            .unique()
        )
    )


# =========================================================
# BUILDING DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">🏢 Building Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    flat_floor = st.number_input(
        "Flat Floor",
        min_value=0,
        value=1,
        step=1
    )


with col2:

    total_floors = st.number_input(
        "Total Floors",
        min_value=0,
        value=5,
        step=1
    )


with col3:

    parking_numbers = st.number_input(
        "Parking Numbers",
        min_value=0,
        value=0,
        step=1
    )


# =========================================================
# OTHER DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">🛋️ Other Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    parking_type = st.selectbox(
        "Parking Type",
        sorted(
            df.loc[
                df["Parking Type"] != "Unknown",
                "Parking Type"
            ]
            .dropna()
            .unique()
        )
    )


with col2:

    furnishing = st.selectbox(
        "Furnishing",
        sorted(
            df.loc[
                df["Furnishing"] != "Unknown",
                "Furnishing"
            ]
            .dropna()
            .unique()
        )
    )


with col3:

    transaction = st.selectbox(
        "Transaction Type",
        sorted(
            df.loc[
                df["Transaction"] != "Unknown",
                "Transaction"
            ]
            .dropna()
            .unique()
        )
    )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    predict_button = st.button(
        "🔮 Predict House Price",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # Create input data

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

    if prediction < 0:
        prediction = 0.01

    if prediction < 1:
        price = prediction * 100
        price_text = f"₹ {price:.2f} Lakhs"
    else:
        price_text = f"₹ {prediction:.2f} Crores"

    st.markdown("---")

    st.markdown(
        "<h3 style='text-align:center;'>🏠 Estimated House Price</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h1 style='text-align:center;'>{price_text}</h1>",
        unsafe_allow_html=True
    )
