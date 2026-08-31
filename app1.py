import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

df = pd.read_csv("cleaned-home-data.csv")

with open("pipe.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction")

st.subheader("📍 Location Details")

states = sorted(df["state"].dropna().unique())

selected_state = st.selectbox(
    "Select State",
    states
)

locations = sorted(
    df.loc[df["state"] == selected_state, "Location"]
    .dropna()
    .unique()
)

selected_location = st.selectbox(
    "Select Location",
    locations
)

st.subheader("🏠 Property Details")

carpet_area = st.number_input(
    "Carpet Area",
    min_value=0,
    value=500,
    step=100
)

bhk = st.selectbox(
    "BHK",
    sorted(df["BHK"].dropna().unique())
)

bathroom = st.selectbox(
    "Bathroom",
    sorted(df["Bathroom"].dropna().unique())
)

balcony = st.selectbox(
    "Balcony",
    sorted(df["Balcony"].dropna().unique())
)

st.subheader("🏢 Building Details")

flat_floor = st.number_input(
    "Flat Floor",
    min_value=0,
    value=1,
    step=1
)

total_floors = st.number_input(
    "Total Floors",
    min_value=0,
    value=5,
    step=1
)

parking_numbers = st.number_input(
    "Parking Numbers",
    min_value=0,
    value=0,
    step=1
)
st.subheader("🛋️ Other Details")

parking_type = st.selectbox(
    "Parking Type",
    sorted(
        df.loc[df["Parking Type"] != "Unknown", "Parking Type"]
        .dropna()
        .unique()
    )
)

furnishing = st.selectbox(
    "Furnishing",
    sorted(
        df.loc[df["Furnishing"] != "Unknown", "Furnishing"]
        .dropna()
        .unique()
    )
)

transaction = st.selectbox(
    "Transaction",
    sorted(
        df.loc[df["Transaction"] != "Unknown", "Transaction"]
        .dropna()
        .unique()
    )
)

if st.button("🔮 Predict Price"):

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
    prediction = max(0, prediction)

    st.success(f"🏠 Estimated House Price: ₹ {prediction:.2f} Crores")