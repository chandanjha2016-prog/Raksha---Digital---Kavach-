
import streamlit as st

st.set_page_config(page_title="Bihar AI Copilot", page_icon="🤖", layout="centered")

st.title("🤖 Bihar AI Copilot")
st.subheader("BIHARI FIRST. Jo pucho wahi jawab")

question = st.text_input("Apna sawal Hindi me likho")

if st.button("Jawab Do"):
    if question:
        st.info(f"Tumne pucha: {question}")
        st.write("Jawab: Main Bihar Sarkar ki AI hu. Aapki madad ke liye taiyaar hu.")
    else:
        st.warning("Pehle sawal likho bhai")

st.markdown("---")
st.write("Made in Bihar | For Farmers, Students, Everyone")
