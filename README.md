
# ISS Real-Time Tracking System

This project provides a real-time tracking interface for the International Space Station (ISS) using Streamlit and Folium. It fetches the latest location of the ISS from the [Open Notify API](http://api.open-notify.org) and displays the position on an interactive map with automatic updates every 5 seconds.

## Features

- **Real-time updates**: Auto-refresh every 5 seconds to display the latest ISS position.
- **Interactive Map**: Visualize the ISS location on an interactive Folium map.
- **Open Notify API**: Uses a public API to fetch the current position of the ISS.

## Installation

### Prerequisites
- Python 3.x
- `pip` for managing Python packages

### Clone the Repository
```bash
git clone https://github.com/your-username/iss-tracking.git
cd iss-tracking
```

### Install Dependencies
```bash
pip install streamlit folium requests streamlit-folium streamlit-autorefresh
```

## How to Run

1. Open a terminal or command prompt in the project directory.
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open your browser at `http://localhost:8501` to access the application.

## Code Overview

### `app.py`

```python
import folium
import streamlit as st
from streamlit_folium import st_folium
import requests
from streamlit_autorefresh import st_autorefresh

# API endpoint for the ISS location
API_URL = "http://api.open-notify.org/iss-now.json"

# Function to fetch the ISS location
def get_new_position():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])
    except Exception as e:
        st.error(f'Error fetching data: {e}')
        return None, None

# Auto-refresh every 5 seconds
st_autorefresh(interval=5000, key="iss_tracking")

# Streamlit app layout
st.title("ISS Real-Time Tracking System")

# Fetch the new position of the ISS
lat, lon = get_new_position()

# Create a Folium map and add a marker at the ISS position if available
m = folium.Map(location=[0, 0], zoom_start=2)
if lat is not None and lon is not None:
    folium.Marker([lat, lon], popup="ISS").add_to(m)
    m.location = [lat, lon]

# Display the map with st_folium
st_folium(m, width=700, height=500)
```

## How it Works

1. **Fetching ISS Position**: The app sends a request to the [Open Notify API](http://api.open-notify.org/iss-now.json) to get the current latitude and longitude of the ISS.
2. **Displaying on Map**: If the position is successfully fetched, the ISS's current location is marked on a Folium map.
3. **Auto-Refresh**: The app uses `streamlit-autorefresh` to update the ISS position every 5 seconds.

## Troubleshooting

- If the Open Notify API is down, the app may show an error. Try again after some time.
- Ensure all dependencies are installed correctly with `pip install -r requirements.txt`.

## Future Improvements

- Add historical tracking of the ISS path.
- Display information about the next passes of the ISS over your location.
- Optimize the interface for mobile devices.
