import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pickle
from prophet import Prophet
from datetime import timedelta

# Load the model
def load_model():
    with open('facebook_prophet_2.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# Modified Function to Predict Web Traffic
def predict_web_traffic(model, user_type, end_date):
    start_date = model.history['ds'].min()
    date_range = pd.date_range(start=start_date, end=end_date)
    future = pd.DataFrame({'ds': date_range})
    forecast = model.predict(future)
    forecast['yhat_exp'] = np.exp(forecast['yhat'])
    return forecast[['ds', 'yhat_exp']]

# Main app
def main():
    st.title("Web Traffic Prediction")
    image_path = 'Images/Header image.png'
    st.image(image_path, use_column_width=True)

    st.markdown("Our project aims to revolutionize ad placement strategies ...")
    
    with st.expander("How to use this app"):
        st.write("""
            1. Select the user type from the dropdown menu...
        """)
    
        st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #007bff; /* Bootstrap primary color */
            color: white;
        }
        </style>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        user_type = st.selectbox("Select User Type", ('Total Users', 'Unique Users')) 
    with col2:
        selected_date = st.date_input("Select Date")

    if st.button('Predict'):
        with st.spinner('Calculating...'):
            forecast = predict_web_traffic(model, user_type, selected_date)
            selected_prediction = forecast[forecast['ds'] == pd.to_datetime(selected_date)]['yhat_exp'].iloc[0]
            
            st.write(f"Predicted {user_type} on {selected_date.strftime('%Y-%m-%d')} are {selected_prediction}")
            
            plt.figure(figsize=(10, 4))
            plt.plot(forecast['ds'], forecast['yhat_exp'], label='Prediction Trend')
            plt.scatter([selected_date], [selected_prediction], color='red', label='Selected Date Prediction')
            plt.title(f'Predicted Web Traffic Trend for {user_type}')
            plt.xlabel('Date')
            plt.ylabel('Number of Users')
            plt.legend()
            plt.grid()
            st.pyplot(plt)

if __name__ == "__main__":
    main()
