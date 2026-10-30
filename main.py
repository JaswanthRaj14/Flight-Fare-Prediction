from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

from enum import Enum
from pydantic import BaseModel, Field, model_validator


app = FastAPI(title="Flight Fare Prediction API",
              description="API for Flight Fare Prediction",
              version="1.0.0")

model = joblib.load("flight_fare_model.pkl")



class Airline(str, Enum):
    air_asia = "Air Asia"
    air_india = "Air India"
    goair = "GoAir"
    indigo = "IndiGo"
    jet_airways = "Jet Airways"
    jet_airways_business = "Jet Airways Business"
    multiple_carriers = "Multiple carriers"
    multiple_carriers_premium = "Multiple carriers Premium economy"
    spicejet = "SpiceJet"
    trujet = "Trujet"
    vistara = "Vistara"
    vistara_premium = "Vistara Premium economy"


class Source(str, Enum):
    banglore = "Banglore"
    chennai = "Chennai"
    delhi = "Delhi"
    kolkata = "Kolkata"
    mumbai = "Mumbai"


class Destination(str, Enum):
    banglore = "Banglore"
    cochin = "Cochin"
    delhi = "Delhi"
    hyderabad = "Hyderabad"
    kolkata = "Kolkata"
    new_delhi = "New Delhi"


class AdditionalInfo(str, Enum):
    long_layover = "1 long layover"
    short_layover = "1 short layover"
    two_long_layovers = "2 long layover"
    business_class = "business class"
    change_airports = "change airports"
    meal_not_included = "in-flight meal not included"
    baggage_not_included = "no check-in baggage included"
    no_info = "no info"
    red_eye = "red-eye flight"


class FlightDetails(BaseModel):
    Airline: Airline
    Source: Source
    Destination: Destination
    Total_Stops: int = Field(ge=0, le=4)
    Duration_Minutes: int = Field(gt=0)
    Journey_Day: int = Field(ge=1, le=31)
    Journey_Month: int = Field(ge=1, le=12)
    Dep_Hour: int = Field(ge=0, le=23)
    Dep_Minute: int = Field(ge=0, le=59)
    Arrival_Hour: int = Field(ge=0, le=23)
    Arrival_Minute: int = Field(ge=0, le=59)
    Additional_Info: AdditionalInfo

    @model_validator(mode="after")
    def validate_route(self):
        if self.Source.value == self.Destination.value:
            raise ValueError("Source and destination must be different")
        return self


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Flight Fare Prediction API",
        "status": "API is running"
    }


# Prediction endpoint
@app.post("/predict")
def predict_fare(flight: FlightDetails):

    input_data = pd.DataFrame([flight.model_dump()])

    prediction = model.predict(input_data)

    return {
        "predicted_fare": round(float(prediction[0]), 2),
        "currency": "INR"
    }
