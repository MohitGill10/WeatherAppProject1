import streamlit as st
import pandas as pd

# Set up Streamlit app configuration - must be the first Streamlit command
st.set_page_config(page_title="Weather Dashboard", layout="wide")

# Load data from CSV
@st.cache_data  # Caches data to optimize performance
def load_data():
    return pd.read_csv("Cleaned_GlobalWeather.csv")

# Load data
data = load_data()

# Title and introductory text
st.title("Global Weather Dashboard")
st.markdown("Use the filters on the sidebar to view specific weather data.")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_date = st.sidebar.date_input("Select Date")  # Date picker filter
selected_country = st.sidebar.selectbox("Select Country", options=data["country"].unique())
min_temp = st.sidebar.slider("Minimum Temperature (°C)", float(data["temperature_celsius"].min()), float(data["temperature_celsius"].max()))

# Apply filters to the DataFrame
filtered_data = data[
    (pd.to_datetime(data["last_updated"], format='%d/%m/%Y %H:%M').dt.date == selected_date) &
    (data["country"] == selected_country) &
    (data["temperature_celsius"] >= min_temp)
]

# Display filtered data
st.subheader("Filtered Weather Data")
st.write(f"Showing data for {selected_country} on {selected_date}")
st.dataframe(filtered_data)

# Display summary statistics
st.subheader("Summary Statistics")
st.write(filtered_data.describe())

# Plotting temperature and precipitation
st.subheader("Temperature and Precipitation Analysis")
st.line_chart(filtered_data.set_index("last_updated")[["temperature_celsius", "precip_mm"]])

# Additional plots (Optional)
st.subheader("Humidity and Wind Analysis")
st.line_chart(filtered_data.set_index("last_updated")[["humidity", "wind_kph"]])

st.markdown("**Data source**: CSV file - Cleaned_GlobalWeather.csv")
