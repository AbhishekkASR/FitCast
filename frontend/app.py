import streamlit as st
import requests

st.title("FitCast AI Fashion Recommendation")

file = st.file_uploader("Upload Outfit Image")

API_URL = "https://fitcast-api.onrender.com/recommend"

if file:

    st.image(file)

    response = requests.post(API_URL,files={"file":file})

    data = response.json()

    st.subheader("Recommended Styles")

    for img in data["recommendations"]:

        st.image(img,width=200)

    st.subheader("Products")

    for p in data["products"]:

        st.image(p["image"],width=150)

        st.write(p["name"])

        st.write("Price:",p["price"])