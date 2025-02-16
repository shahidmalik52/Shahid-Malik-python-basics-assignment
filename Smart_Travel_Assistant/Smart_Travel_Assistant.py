# Assignment Overview
    # You will build a Smart Travel Assistant using Python and Streamlit. The app will:
    # Let users select a travel destination.
    # Estimate travel expenses based on user input.
    # Suggest a packing checklist based on the expected weather.
    # Display a travel summary with all user inputs

# Task 1: User Destination Selection
    # The user selects a destination from a list of famous cities.
    # The user chooses the expected weather condition (Sunny, Rainy, Cold).
    # The app stores the user’s choice and displays it on the screen.

import streamlit as st
cities = ['Lahore', 'Islamabad', 'Murree']                                                          # List of cities
weather = ['Sunny', 'Rainy', 'Cold']                                                                # List of weather conditions
st.title('Smart Travel Assistant by Shahid Malik')                                                  # App title
chosen_city = st.selectbox( "Choose your desired city: ", cities, index = None )                    # User selects a city
chosen_weather = st.selectbox( "Choose your expected weather condition: ", weather, index= None )   # User selects a weather condition
if chosen_city and chosen_weather:                                                                  # If user has selected a city and weather
    st.write(f"You have selected {chosen_city} city and {chosen_weather} weather")                  # Display user's choice

# Task 2: Travel Expense Calculator
    # The user enters the number of travel days.
    # The user enters their daily budget (food, transport, sightseeing, etc.).
    # The app calculates the total estimated travel cost.
    # The user can add optional expenses (e.g., flight cost, hotel booking).
    # The total trip cost is displayed in the app.

total_estimated_travel_cost = 0
num_of_days = st.number_input('Enter the number of travel days: ', min_value=1, max_value=30)                   # User enters the number of travel days
daily_budget = st.number_input('Enter your daily budget: (food, transport, sightseeing, etc.) ')                # User enters their daily budget
additional_expense = st.number_input('Enter additional expenses like flight cost, hotel booking (if any): ')    # User enters additional expenses
if num_of_days and daily_budget and additional_expense:                                                         # If user has entered the number of travel days, daily budget and additional expenses
    total_estimated_travel_cost = (num_of_days * daily_budget) + additional_expense                               # Calculate total estimated travel cost
    st.write(f"Total estimated travel cost: {total_estimated_travel_cost}")                                     # Display total estimated travel cost   

# Task 3: Packing Checklist Generator
    # Based on the selected weather condition, the app suggests a packing list.
    # For Rainy weather, it suggests Umbrella, Raincoat, Waterproof Shoes.
    # For Cold weather, it suggests Jacket, Gloves, Warm Clothes.
    # For Sunny weather, it suggests Sunglasses, Sunscreen, Hat.
    # The user can modify the packing list by adding or removing items.

checklist = []
if chosen_weather == 'Cold':
    checklist = ['Jacket', 'Gloves', 'Warm Clothes']                                                                                             # If user has selected Cold weather
elif chosen_weather == 'Rainy':
    checklist = ['Umbrella', 'Raincoat', 'Waterproof Shoes']
elif chosen_weather == 'Sunny':
    checklist = ['Sunglasses', 'Sunscreen', 'Hat']

if chosen_weather:                                                                                                                         # If user has selected a weather condition
    st.write(f'Based on {chosen_weather} weather, suggested packing list is:')                                      
    st.write(checklist)

additional_items = st.text_input('Do you want to add or remove items from the checklist: A/R otherwise press any key').upper()
if additional_items == 'A':
    item_to_add = st.text_input('Enter item to add: ').title()
    checklist.append(item_to_add)
elif additional_items == 'R':
    item_to_remove = st.text_input('Enter item to remove: ').title()
    if item_to_remove in checklist:
        checklist.remove(item_to_remove)    
if additional_items == 'A' or additional_items =='R':
    st.write(f'Updated packing list is: ')                                                                 # Display updated checklist
    st.write(checklist)

# Task 4: Travel Summary & File Saving
    # The app displays a final travel summary, including:
        # Destination
        # Weather Condition
        # Total Trip Cost
        # Packing List
    # The user can save their travel details to a file for future reference.
    # The app allows users to view past travel plans.

summary = st.button('Summary')
if summary:
    st.write("### Travel Summary")
    st.write(f"**Destination:** {chosen_city}")
    st.write(f"**Weather Condition:** {chosen_weather}")
    st.write(f"**Total Trip Cost:** {total_estimated_travel_cost}")
    st.write(f"**Packing List:** {checklist}")

    file = open('Smart_Travel.txt', 'w') 
    file.write("Travel Summary\n")
    file.write(f"Destination: {chosen_city}\n")
    file.write(f"Weather Condition: {chosen_weather}\n")
    file.write(f"Total Trip Cost: {total_estimated_travel_cost}\n")
    file.write(f"Packing List: {checklist}\n")
    file.close()


import datetime
expected_date = st.date_input("Choose your expected dates of visit", datetime.date(2025, 2, 13))
if expected_date:
    st.write("Your selected date is:", expected_date)
current_date = datetime.date.today()
days_left = (expected_date - current_date).days
if days_left > 0:
    st.success(f"{days_left} days left for your trip to start! 🎉")
elif days_left == 0:
    st.warning("Your trip starts today! ✈️")
else:
    st.error("The selected date is in the past! ❌")

