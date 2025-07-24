import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("CrimeMap+")

st.write("Upload a crime data CSV or use the default Minneapolis sample.")

uploaded_file = st.file_uploader("Upload your crime data CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using placeholder dataset.")
    df = pd.DataFrame({
        'Latitude': [44.9778],
        'Longitude': [-93.2650],
        'Description': ['Theft']
    })

m = folium.Map(location=[44.9778, -93.2650], zoom_start=12)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        popup=row['Description'],
        fill=True,
        color='red'
    ).add_to(m)

st_data = st_folium(m, width=700)
