import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Placeholder function for your predictive model
def predict_web_traffic(user_type, date):
    # Replace with your own model logic
    # This function currently returns random data for demonstration purposes
    return np.random.randint(100, 500)

# Main app
def main():
    st.title("Web Traffic Prediction")

    # Display the image
    image_path = 'Images/Header image.png'
    st.image(image_path, use_column_width=True)

    st.markdown("Our project aims to revolutionize ad placement strategies through advanced Time Series Forecasting for Jambojet to optimize its advertising spaces to maximize revenue.", unsafe_allow_html=True)

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
        prediction = predict_web_traffic(user_type, selected_date)

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


