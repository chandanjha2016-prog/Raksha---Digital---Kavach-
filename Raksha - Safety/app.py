import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="RAKSHA KAR MAA", page_icon="🇮🇳")
st.title("🇮🇳 RAKSHA DIGITAL KAVACH")
st.write("AI Road Safety Prediction - Educational Demo")

# Model Load
# scaler = pickle.load(open('scaler.pkl', 'rb')) # abhi comment rakho

st.warning("Disclaimer: Ye educational purpose ke liye hai. 100% accurate nahi hai.")

# Form
speed = st.number_input("Speed (km/h)", 0, 200, 60)
st.button("Predict")

st.success("App Live ho gaya! Ab model add karenge.")
