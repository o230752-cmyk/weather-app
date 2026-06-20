import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Weather Site", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Full black background */
.stApp {
    background-color: #000000;
}

/* White text everywhere */
html, body, [class*="css"] {
    color: white !important;
}

/* Title */
h1 {
    color: white !important;
    font-size: 55px !important;
    font-weight: 800 !important;
}

/* Input box */
div[data-baseweb="input"] input {
    background-color: #111111 !important;
    color: white !important;
    border: 2px solid #ff3b3b !important;
    border-radius: 10px !important;
}

/* Submit button */
.stButton > button,
button[kind="primary"] {
    background-color: white !important;
    color: black !important;
    font-weight: bold !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 10px 25px !important;
}

.stButton > button:hover {
    background-color: #f0f0f0 !important;
}

/* Weather result box */
.weather-box {
    border: 2px solid #ff3b3b;
    border-radius: 15px;
    padding: 25px;
    margin-top: 20px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("WEATHER SITE:")

# ---------------- API KEY ----------------
API_KEY = "a5986c124cebd97ca6a083194aa7c2d4"

# ---------------- FORM ----------------
with st.form("weather_form"):
    city = st.text_input("Enter city name for weather status")
    submit = st.form_submit_button("Submit")

# ---------------- WEATHER DATA ----------------
if submit:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        st.markdown(f"""
        <div class="weather-box">
            <h3>Weather Information</h3>
            <p><b>City:</b> {data['name']}</p>
            <p><b>Temperature:</b> {data['main']['temp']} °C</p>
            <p><b>Humidity:</b> {data['main']['humidity']} %</p>
            <p><b>Weather:</b> {data['weather'][0]['description'].title()}</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.error("City not found!")