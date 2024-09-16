import streamlit as st
import joblib
import numpy as np
from sklearn.datasets import load_breast_cancer
import tensorflow as tf
from tensorflow import keras

# Load Breast Cancer dataset
data = load_breast_cancer()
feature_names = data.feature_names
class_names = data.target_names

# Load the trained Logistic Regression model (ML)
modelML = joblib.load('logistic_regression_model.pkl')

# Load the trained MLP model (DL)
modelDL = keras.models.load_model('neural_network_model.h5')

# Title and description
st.title('Breast Cancer Prediction App')
st.write("This app predicts whether a breast tumor is malignant or benign based on user input features.")

# Create input fields for each feature in the dataset (allow full decimal precision)
inputs = []
for feature in feature_names:
    value = st.number_input(f"{feature}", min_value=0.0, format="%.10f", step=0.00000001)
    inputs.append(value)

# Convert input data to numpy array
user_input = np.array([inputs])

# Model selection (ML or DL)
model_type = st.selectbox("Choose Model Type", ("Logistic Regression (ML)", "MLP Neural Network (DL)"))

# When the user clicks the Predict button
if st.button('Predict'):
    if model_type == "Logistic Regression (ML)":
        # Make prediction using the ML model (Logistic Regression)
        predictionML = modelML.predict(user_input)
        st.write(f"Prediction using Logistic Regression: {class_names[predictionML][0]}")

    elif model_type == "MLP Neural Network (DL)":
        # Make prediction using the DL model (MLP)
        predictionDL = modelDL.predict(user_input)
        
        # Since the DL model output is a probability, classify it based on threshold 0.5
        if predictionDL[0][0] >= 0.5:
            prediction = class_names[1]  # Benign
        else:
            prediction = class_names[0]  # Malignant

        st.write(f"Prediction using MLP Neural Network: {prediction}")
