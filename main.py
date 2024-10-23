import folium
import streamlit as st
from streamlit_folium import st_folium
import requests
from streamlit_autorefresh import st_autorefresh

# API endpoint to get the current position of the ISS
API_URL = "http://api.open-notify.org/iss-now.json"

# Function to fetch the new position of the ISS
def get_new_position():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])
    except Exception as e:
        st.error(f'Error fetching data: {e}')
        return None, None

# Auto-refresh every 5 seconds (5000ms)
st_autorefresh(interval=5000, key="iss_tracking")

# Streamlit app layout
st.title("ISS Real-Time Tracking System")

# Fetch the new position of the ISS
lat, lon = get_new_position()

# Create a Folium map and add a marker at the ISS position, if available
m = folium.Map(location=[0, 0], zoom_start=2)
if lat is not None and lon is not None:
    folium.Marker([lat, lon], popup="ISS").add_to(m)
    m.location = [lat, lon]

# Display the map using st_folium
st_folium(m, width=700, height=500)
