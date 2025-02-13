import streamlit as st
import requests
import datetime

# OpenWeatherMap API Key (Replace with your own key)
API_KEY = "5240efa02cc404a048b1413c92d1786c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

st.title("🌤️ Real-Time Weather App")

city = st.text_input("🏙️ Enter city name:")
if st.button("🔍 Get Weather"):
    if city:
        data = get_weather(city)
        if data["cod"] == 200:
            st.success(f"🌍 Weather in {city.capitalize()}:")
            st.write(f"🌡️ Temperature: {data['main']['temp']}°C")
            st.write(f"☁️ Weather: {data['weather'][0]['description'].capitalize()}")
            st.write(f"💧 Humidity: {data['main']['humidity']}%")
            st.write(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
            st.write(f"🌅 Sunrise: {datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')}")
            st.write(f"🌇 Sunset: {datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')}")
        else:
            st.error("❌ City not found. Please enter a valid city name.")
    else:
        st.warning("⚠️ Please enter a city name.")
