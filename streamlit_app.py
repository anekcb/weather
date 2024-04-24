import streamlit as st
import requests
import json

# Create a Streamlit app
st.title("Weather App")
st.markdown("Enter your OpenWeatherMap API key and location to get the current weather")

# Get the user's API key
api_key = st.text_input("OpenWeatherMap API Key")

# Get the user's location
location = st.text_input("Location")

# Set the base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

if st.button("Get Weather"):
    if api_key:
        # Make a GET request to the OpenWeatherMap API
        response = requests.get(f"{BASE_URL}?q={location}&appid={api_key}&units=metric")

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Get the weather data
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            # Display the weather data
            st.markdown(f"Weather: {weather}")
            st.markdown(f"Temperature: {temperature}°C")
            st.markdown(f"Humidity: {humidity}%")
            st.markdown(f"Wind Speed: {wind_speed} m/s")
        else:
            st.error("Failed to retrieve weather data")
    else:
        st.error("Please enter your OpenWeatherMap API key")
