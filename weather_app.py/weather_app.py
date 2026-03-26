import streamlit as st
import requests

API_KEY = "your_api_key_here"

st.title("🌦️ Real-Time Weather App")

city = st.text_input("Enter City Name")

unit = st.selectbox("Select Unit", ["Celsius", "Fahrenheit"])

if st.button("Get Weather"):
    if city:
        if unit == "Celsius":
            units = "metric"
        else:
            units = "imperial"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"

        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            st.error("City not found!")
        else:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]

            icon_url = f"http://openweathermap.org/img/wn/{icon}.png"

            st.image(icon_url)
            st.write(f"🌡️ Temperature: {temp}°")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"🌤️ Weather: {weather}")

    else:
        st.warning("Please enter a city name")