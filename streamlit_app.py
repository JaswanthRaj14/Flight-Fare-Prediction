
import streamlit as st
import joblib
import pandas as pd

from pathlib import Path
from datetime import date, time


# --------------------------------------------------
# 1. Load trained ML model
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "flight_fare_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


# --------------------------------------------------
# 2. Streamlit page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Flight Fare Predictor",
    page_icon="✈️",
    layout="centered"
)


# --------------------------------------------------
# 3. Application heading
# --------------------------------------------------

st.title("✈️ Flight Fare Prediction")

st.write(
    "Enter your flight details below to estimate "
    "the flight ticket fare using Machine Learning."
)


# --------------------------------------------------
# 4. Dropdown options
# --------------------------------------------------

airlines = [
    "Air Asia",
    "Air India",
    "GoAir",
    "IndiGo",
    "Jet Airways",
    "Jet Airways Business",
    "Multiple carriers",
    "Multiple carriers Premium economy",
    "SpiceJet",
    "Trujet",
    "Vistara",
    "Vistara Premium economy"
]

sources = [
    "Banglore",
    "Chennai",
    "Delhi",
    "Kolkata",
    "Mumbai"
]

destinations = [
    "Hyderabad",
    "Cochin",
    "Delhi",
    "Banglore",
    "Kolkata",
    "New Delhi"
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


# --------------------------------------------------
# 5. Flight details form
# --------------------------------------------------

with st.form("flight_form"):

    st.subheader("Flight Information")

    airline = st.selectbox(
        "Airline",
        airlines
    )

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox(
            "Source",
            sources
        )

    with col2:
        destination = st.selectbox(
            "Destination",
            destinations
        )

    total_stops = st.selectbox(
        "Number of Stops",
        [0, 1, 2, 3, 4]
    )

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

    info = st.selectbox(
        "Additional Information",
        additional_info
    )

    submitted = st.form_submit_button(
        "Predict Flight Fare"
    )


# --------------------------------------------------
# 6. Prediction
# --------------------------------------------------

if submitted:

    if source == destination:

        st.error(
            "Source and destination must be different."
        )

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

            input_data = pd.DataFrame([payload])

            prediction = model.predict(input_data)

            predicted_fare = float(prediction[0])

            st.success(
                "Flight fare prediction completed successfully!"
            )

            st.metric(
                label="Estimated Flight Fare",
                value=f"₹{predicted_fare:,.2f}"
            )

            st.caption(
                "This is an estimated fare generated "
                "by the Machine Learning model."
            )

        except Exception as e:

            st.error(
                f"An error occurred during prediction: {e}"
            )
