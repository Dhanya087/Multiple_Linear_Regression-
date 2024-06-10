# Startup Profit Prediction using Multiple Linear Regression

This project demonstrates a machine learning model that predicts startup profits based on R&D spend, administration expenses, marketing spend, and the state in which the startup operates. The model is built using Python and includes an interactive web application powered by Streamlit to visualize the predictions.

## Project Overview
The goal of this project is to predict a startup's profit based on its expenditures and location. We utilize a Multiple Linear Regression algorithm to model the relationship between the input features and the target variable (profit). The project includes:

- Data preprocessing and encoding categorical variables
- Training the Multiple Linear Regression model
- An interactive Streamlit app to visualize predictions

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/startup-profit-prediction.git
    cd startup-profit-prediction
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To run the Streamlit app and see the profit predictions:

1. Ensure you are in the project directory:
    ```sh
    cd path/to/your/project
    ```

2. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to interact with the app.

## Features
- Predict startup profits based on R&D spend, administration expenses, marketing spend, and state
- Interactive visualizations using Streamlit
- Easy-to-use interface for inputting data and viewing results
