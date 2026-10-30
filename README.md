# ✈️ Flight Fare Prediction

An end-to-end Machine Learning project that analyzes flight data and predicts estimated airline ticket fares using an Extra Trees Regressor. The trained model is integrated into a Streamlit web application and deployed on Streamlit Community Cloud.

## 🌐 Live Demo

**[Launch Flight Fare Prediction App](https://flight-fare-prediction-f3coqgewgrkjfjk6uykqfe.streamlit.app/)**

## 📌 Project Overview

Flight ticket prices vary depending on several factors, including airline, route, journey date, number of stops, flight duration, and additional flight information.

The objective of this project is to analyze these factors, develop a regression model, and build an interactive application that estimates flight fares based on user-provided details.

## 🎯 Objectives

- Perform data cleaning and preprocessing.
- Explore patterns and relationships in flight fares.
- Engineer meaningful features for model development.
- Train and compare multiple regression algorithms.
- Evaluate model performance using appropriate regression metrics.
- Develop a prediction API using FastAPI.
- Build an interactive frontend using Streamlit.
- Deploy the application online.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model | Extra Trees Regressor |
| Backend API | FastAPI |
| Frontend | Streamlit |
| Model Serialization | Joblib |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## 📂 Dataset

The dataset contains flight information and ticket prices.

Important features include:

- Airline
- Source and Destination
- Journey Date
- Departure and Arrival Time
- Flight Duration
- Total Stops
- Additional Information
- Price (Target Variable)

## 🔍 Data Preparation and Feature Engineering

The original dataset contained 10,683 records.

The following preprocessing activities were performed:

- Removed 220 duplicate records.
- Removed records with missing route and stop information.
- Handled inconsistent date and time formats.
- Converted flight duration into minutes.
- Extracted journey day and month.
- Extracted departure and arrival hours and minutes.
- Converted total stops into numerical values.
- Standardized categorical values.

The resulting cleaned dataset contained 10,462 records.

## 📊 Exploratory Data Analysis

Explored the relationship between flight prices and:

- Airlines
- Number of stops
- Flight duration
- Journey month
- Source and destination
- Additional flight information

EDA helped identify differences in fare distributions across airlines and routes.

## 🤖 Model Development

The following regression algorithms were evaluated:

- Linear Regression
- Random Forest Regressor
- Extra Trees Regressor

### Model Evaluation

The leading Extra Trees model achieved the following results:

| Metric | Result |
|---|---:|
| MAE | ₹643.17 |
| RMSE | ₹1,509.57 |
| R² Score | 0.8907 |
| 5-Fold CV Mean MAE | ₹663.33 |
| 5-Fold CV MAE Std | ₹17.14 |

The original Extra Trees model was selected based on its cross-validation MAE among the evaluated candidates.

*Note: These are experimental results from the project. The test set was inspected during model experimentation, so the reported test metrics should not be interpreted as an untouched final evaluation.*

## 🏗️ Application Architecture

1. User enters flight information through Streamlit.
2. Streamlit converts the input into a DataFrame.
3. The saved ML pipeline processes the input.
4. Extra Trees Regressor generates a fare prediction.
5. Streamlit displays the estimated fare.

FastAPI is also implemented as a separate prediction API.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/JaswanthRaj14/Flight-Fare-Prediction.git
cd Flight-Fare-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

Open the local URL displayed in your terminal.

### 5. Run the FastAPI backend separately

```bash
python -m uvicorn main:app --reload
```

Open the API documentation at:

```text
http://127.0.0.1:8000/docs
```

## 📁 Project Structure

```text
Flight-Fare-Prediction/
│
├── Data/
│
├── flight_fare_model.pkl
├── Flight_fare_prediction.ipynb
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔮 Future Improvements

- Improve model generalization through further validation and tuning.
- Add more robust input validation.
- Explore additional features and model alternatives.
- Improve the application's user interface.
- Monitor model performance and prediction errors.

## 👨‍💻 Author

**Jaswanth Raj**

GitHub: [JaswanthRaj14](https://github.com/JaswanthRaj14)

---

⭐ If you find this project interesting, feel free to explore the repository and try the live application.
