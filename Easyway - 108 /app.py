
import streamlit as st

st.set_page_config(page_title="Easyway 108", page_icon="🚑", layout="centered")

st.title("🚑 Easyway - 108")
st.subheader("BIHAR FIRST. Voice se Ambulance Bulao")

name = st.text_input("Naam")
location = st.text_input("Location - GPS On kare")
problem = st.selectbox("Problem", ["Heart Attack", "Accident", "Delivery", "Other"])

if st.button("🔴 108 CALL KARO ABHI"):
    st.success(f"Ambulance bhej di gayi hai {location} par!")
    st.balloons()
    
st.markdown("---")
st.write("Made in Patna, Bihar | Made for 8 Billion People")
