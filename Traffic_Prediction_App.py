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
    # Assuming 'yhat' is the predicted log-transformed value
    prediction = np.exp(forecast['yhat'].iloc[0])

    return prediction


# Main app
def main():
    st.title("Web Traffic Prediction")

    # Display the image
    image_path = 'Images/Header image.png'
    st.image(image_path, use_column_width=True)

    st.markdown("Our project aims to revolutionize ad placement strategies through advanced Time Series Forecasting for Jambojet to optimize its advertising spaces to maximize revenue.", unsafe_allow_html=True)

    # Collapsible Instructions
    with st.expander("How to use this app"):
        st.write("""
            1. Select the user type from the dropdown menu.
            2. Choose the date for which you want to predict web traffic.
            3. Click on 'Predict' to view the results.
        """)

    # Custom button color
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #df006e;
            color: white;
        }
        </style>""", unsafe_allow_html=True)

    # User selection and Date selection on the same line
    col1, col2 = st.columns(2)
    with col1:
        user_type = st.selectbox("Select User Type", ('New Users', 'Total Users'))
    with col2:
        selected_date = st.date_input("Select Date")

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