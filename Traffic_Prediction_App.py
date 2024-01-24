import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pickle
from fbprophet import Prophet

# Load the model
@st.cache
def load_model():
    with open('facebook_prophet.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# Function to predict web traffic
def predict_web_traffic(model, user_type, date):
    # Assuming your model expects a DataFrame with a ds column for dates
    future = pd.DataFrame({'ds': [pd.to_datetime(date)]})

    # Generate the forecast
    forecast = model.predict(future)

    # Convert the log-transformed prediction back to the original scale
    # Assuming your 'yhat' is the predicted log-transformed value
    prediction = np.exp(forecast['yhat'].iloc[0])

    return prediction

# Main app function remains largely the same
def main():
    # ... existing code ...

    # Predict button at the bottom
    if st.button('Predict'):
        with st.spinner('Calculating...'):
            prediction = predict_web_traffic(model, user_type, selected_date)

            # Displaying the prediction
            if user_type == 'New Users':
                st.write(f"Predicted new users are {prediction}")
            else:
                st.write(f"Predicted total users are {prediction}")

            # Plotting
            plt.figure(figsize=(10, 4))
            plt.plot([selected_date], [prediction], marker='o')
            plt.title(f'Predicted Web Traffic for {user_type}')
            plt.xlabel('Date')
            plt.ylabel('Number of Users')
            st.pyplot(plt)

if __name__ == "__main__":
    main()

