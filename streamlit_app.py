
import streamlit as st
import requests
from datetime import date, time

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Flight Fare Predictor",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Flight Fare Prediction")
st.write("Enter your flight details to estimate the ticket fare.")

airlines = [
    "Air Asia", "Air India", "GoAir", "IndiGo",
    "Jet Airways", "Jet Airways Business",
    "Multiple carriers", "Multiple carriers Premium economy",
    "SpiceJet", "Trujet", "Vistara", "Vistara Premium economy"
]

sources = ["Banglore", "Chennai", "Delhi", "Kolkata", "Mumbai"]

destinations = [
    "Hyderabad", "Cochin", "Delhi",
    "Banglore", "Kolkata", "New Delhi"
]

additional_info = [
    "1 long layover",
    "1 short layover",
    "2 long layover",
    "business class",
    "change airports",
    "in-flight meal not included",
    "no check-in baggage included",
    "no info",
    "red-eye flight"
]

with st.form("flight_form"):

    st.subheader("Flight Information")

    airline = st.selectbox("Airline", airlines)

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox("Source", sources)

    with col2:
        destination = st.selectbox("Destination", destinations)

    total_stops = st.selectbox("Number of Stops", [0, 1, 2, 3, 4])

    journey_date = st.date_input(
        "Journey Date",
        value=date.today()
    )

    col3, col4 = st.columns(2)

    with col3:
        departure_time = st.time_input(
            "Departure Time",
            value=time(9, 0)
        )

    with col4:
        arrival_time = st.time_input(
            "Arrival Time",
            value=time(12, 0)
        )

    duration_minutes = st.number_input(
        "Total Flight Duration (Minutes)",
        min_value=1,
        value=180
    )

    info = st.selectbox("Additional Information", additional_info)

    submitted = st.form_submit_button("Predict Flight Fare")

if submitted:

    if source == destination:
        st.error("Source and destination must be different.")

    else:
        payload = {
            "Airline": airline,
            "Source": source,
            "Destination": destination,
            "Total_Stops": total_stops,
            "Duration_Minutes": int(duration_minutes),
            "Journey_Day": journey_date.day,
            "Journey_Month": journey_date.month,
            "Dep_Hour": departure_time.hour,
            "Dep_Minute": departure_time.minute,
            "Arrival_Hour": arrival_time.hour,
            "Arrival_Minute": arrival_time.minute,
            "Additional_Info": info
        }

        try:
            response = requests.post(API_URL, json=payload, timeout=30)

            if response.status_code == 200:
                result = response.json()

                st.success("Prediction completed!")

                st.metric(
                    label="Estimated Flight Fare",
                    value=f"₹{result['predicted_fare']:,.2f}"
                )

            else:
                st.error(f"API Error: {response.status_code}")
                st.write(response.json())

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to FastAPI. "
                "Please make sure your backend server is running."
            )
