import streamlit as st
import pandas as pd
import altair as alt
from streamlit import container

st.set_page_config(layout="wide", page_title="Airline Passenger Rating", page_icon = "✈️")



st.title("Airline Passenger Satisfaction")

st.header("Welcome to the Airline Passenger Satisfaction tester!")

st.subheader("By inputing your ratings of your amenities, we can confidently give you a prediction of how satisfied your passengers will be!")

#st.text("This is a simple example of how to use Streamlit to create a website.")

st.image("https://www.shutterstock.com/image-photo/passenger-aircraft-blue-cloudy-sky-260nw-1472463215.jpg", width=1300)




with st.form("my_form"):
    col1, col2, col3, col4, col5 = st.columns([3,3,3,3,4])
    with col1:
        option1 = st.radio("How good is your In-Flight Wi-Fi?", range(6), key='1')
    with col2:
        option2 = st.radio("How good is your Customer Service?", range(6), key='2')
    with col3:
        option3 = st.radio("How good are your In-Flight Meals?", range(6), key='3')
    with col4:
        option4 = st.radio("How good are your airline seats?", range(6), key='4')
    with col5:
        option5 = st.radio("How good is your In-Flight Entertainment?", range(6), key='5')
    calculate_button = st.form_submit_button("Calculate")

if calculate_button:
    total = option1 + option2 + option3 + option4 + option5
    st.write(f"Your passenger's prediction rating is: {total} out of 25")



st.markdown("## Here's how your airline compares with other airlines for your amenities:")
df = pd.DataFrame({
    '_': ['Wi-Fi', 'Customer Service', 'Meals', 'Seats', 'Entertainment'],
     'Your Airline': [option1, option2, option3, option4, option5],
     'Emirates' : [1,2,3,4,5],
     'Singapore Air': [3,4,5,1,2]
})

st.line_chart(df, x='_')
