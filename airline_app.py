# Import necessary libraries
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

airline_df = pd.read_csv('airline.csv')

dt_pickle = open('dt_airline.pickle', 'rb') 
clf = pickle.load(dt_pickle) 
dt_pickle.close()

# Set up the title and description of the app
st.title('Airline Customer Satisfaction') 
st.write("Gain insight into passenger experience and improve satisfaction through data analysis and surveys")
# Display an image of penguins
st.image('airline.jpg', width = 800)

with st.expander("What can you do with this app?"):
    st.markdown("""
    - 📝 **Fill Out a Survey:** Provide a form for users to fill out their airline satisfaction feedback.  
    - 📊 **Make Data-Driven Decisions:** Use insights to guide improvements in customer experience.  
    - 🧩 **Interactive Features:** Explore data with fully interactive charts and summaries!
    """)

# Create a sidebar for input collection
st.sidebar.subheader('Part 1: Customer Details')
st.sidebar.header('**Airline Customer Satisfaction Survey**')
cust = st.sidebar.selectbox('What type of customer is this?', options = ['Loyal Customer','disloyal Customer'])
type_of_travel = st.sidebar.selectbox('Is this customer traveling for business or personal reasons?', options = airline_df['type_of_travel'].unique())
flight_class = st.sidebar.selectbox('In which class will the customer be flying?', options = airline_df['class'].unique())
age = st.sidebar.number_input('How old is the customer?',min_value=airline_df['age'].min(),max_value=airline_df['age'].max(),step=1)

st.sidebar.subheader('Part 2: Flight Details')
flight_distance = st.sidebar.number_input('How far is the customer flying in miles?',min_value=airline_df['flight_distance'].min(),max_value=airline_df['flight_distance'].max(),step=1)
departure_delay = st.sidebar.number_input("How many minutes was the customer's departure delayed?(Enter 0 if not delayed)",min_value=0,max_value=airline_df['departure_delay_in_minutes'].max(),step=1)
arrival_delay = st.sidebar.number_input("How many minutes was the customer's arrival delayed?(Enter 0 if not delayed)",min_value=0,max_value=airline_df['arrival_delay_in_minutes'].max(),step=1)

st.sidebar.subheader('Part 3: Customer Experience')
seat_comfort = st.sidebar.radio(
    'How comfortable was the seat for the customer?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)
departure_arrival_time_convenient = st.sidebar.radio(
    'Was the Departure/Arrival Time convenient for the customer?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

food_and_drink = st.sidebar.radio(
    'How would the customer rate the food and drink?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

gate_location = st.sidebar.radio(
    'How would the customer rate the gate location?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

inflight_wifi_service = st.sidebar.radio(
    'How would the customer rate the in flight wifi service?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

inflight_entertainment = st.sidebar.radio(
    'How would the customer rate the in flight entertainment?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

online_support = st.sidebar.radio(
    'How would the customer rate online support?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

ease_of_online_booking = st.sidebar.radio(
    'How easy was the online booking for the customer?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

on_board_service = st.sidebar.radio(
    'How would the customer rate the onboard service?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

leg_room_service = st.sidebar.radio(
    'How would the customer rate the leg room service?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

baggage_handling = st.sidebar.radio(
    'How would the customer rate baggage handling?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

checkin_service = st.sidebar.radio(
    'How would the customer rate the check-in service?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

cleanliness = st.sidebar.radio(
    'How would the customer rate cleanliness?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

online_boarding = st.sidebar.radio(
    'How would the customer rate online boarding?(1-5 Stars)',
    options=[1, 2, 3, 4, 5],
    horizontal=True,  # makes the buttons appear in one line
)

customer_type_Loyal_Customer, customer_type_disloyal_Customer = 0, 0 
if cust == 'Loyal Customer': 
  customer_type_Loyal_Customer = 1 
elif cust == 'disloyal Customer': 
  customer_type_disloyal_Customer = 1

type_of_travel_Business_travel, type_of_travel_Personal_Travel = 0, 0 
if type_of_travel == 'Personal Travel': 
  type_of_travel_Personal_Travel = 1 
elif type_of_travel == 'Business Travel': 
  type_of_travel_Business_travel = 1

class_Business, class_Eco, class_Eco_Plus = 0,0,0
if flight_class == 'Business': 
  class_Business = 1 
elif flight_class == 'Eco': 
  class_Eco = 1
elif flight_class == 'Eco Plus': 
  class_Eco_Plus = 1

st.title('Prediction of Customer Satisfaction (Decision Tree)')
predict_button = st.sidebar.button("Predict")


if not predict_button:
   st.info("ℹ️ Please fill out the survey form in the sidebar and click **Predict** to see the satisfaction prediction.")

if predict_button:
    new_prediction = clf.predict([[age,flight_distance,seat_comfort,departure_arrival_time_convenient,food_and_drink,gate_location,inflight_wifi_service,
                                inflight_entertainment,online_support,ease_of_online_booking,on_board_service,leg_room_service,baggage_handling,
                                checkin_service,cleanliness,online_boarding,departure_delay,arrival_delay,customer_type_Loyal_Customer,customer_type_disloyal_Customer,
                                type_of_travel_Business_travel,type_of_travel_Personal_Travel,class_Business,class_Eco,class_Eco_Plus]]) 
    prediction_satisfaction = new_prediction[0]

    pred_prob = clf.predict_proba([[age,flight_distance,seat_comfort,departure_arrival_time_convenient,food_and_drink,gate_location,inflight_wifi_service,
                                inflight_entertainment,online_support,ease_of_online_booking,on_board_service,leg_room_service,baggage_handling,
                                checkin_service,cleanliness,online_boarding,departure_delay,arrival_delay,customer_type_Loyal_Customer,customer_type_disloyal_Customer,
                                type_of_travel_Business_travel,type_of_travel_Personal_Travel,class_Business,class_Eco,class_Eco_Plus]]) 

    label_color = "#b33a3a" if prediction_satisfaction.lower() == "dissatisfied" else "#2e7d32"

    st.write("Predicted Satisfaction:",prediction_satisfaction)
    st.write("With a confidence of",pred_prob.max()*100,'%')
    
    with st.expander('Customer Type Comparison'):
        st.write('Customer Type:',cust)
        distribution = airline_df['customer_type'].value_counts(normalize=True)
        st.write('Percentage of our fliers with this selection:',round(distribution.loc[cust],2)*100,'%')

    with st.expander('Type of Travel Comparison'):
        st.write('Type of Travel:',type_of_travel)
        distribution = airline_df['type_of_travel'].value_counts(normalize=True)
        st.write('Percentage of our fliers with this selection:',round(distribution.loc[type_of_travel],2)*100,'%')

    with st.expander('Flight Class Comparison'):
        st.write('Flight Class:',flight_class)
        distribution = airline_df['class'].value_counts(normalize=True)
        st.write('Percentage of our fliers with this selection:',round(distribution.loc[flight_class],2)*100,'%')

    with st.expander('Age Group Comparison'):
        st.write('Age Group:',age)
        distribution = airline_df['age'].value_counts(normalize=True)
        st.write('Percentage of our fliers with this selection:',round(distribution.loc[age],2)*100,'%')





