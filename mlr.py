import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load the dataset
dataset = pd.read_csv('Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encoding Categorical variable
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Splitting the dataset into the Training set and Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# Training the Multiple Linear Regression model on the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Function to predict profit
def predict_profit(RnD_Spend, Administration, Marketing_Spend, State):
    input_data = [[RnD_Spend, Administration, Marketing_Spend, State]]
    input_data_encoded = ct.transform(input_data)
    prediction = regressor.predict(input_data_encoded)
    return prediction[0]

# Streamlit UI
st.title("Startup Profit Prediction")

RnD_Spend = st.number_input("R&D Spend")
Administration = st.number_input("Administration")
Marketing_Spend = st.number_input("Marketing Spend")
State = st.selectbox("State", ["California", "Florida", "New York"])

if st.button("Predict Profit"):
    prediction = predict_profit(RnD_Spend, Administration, Marketing_Spend, State)
    st.write(f"Predicted Profit: {prediction:.2f}")
