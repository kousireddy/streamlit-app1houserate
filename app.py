import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("House Price Prediction")

area = st.number_input("Area")
bed = st.number_input("Bedrooms")
bath = st.number_input("Bathrooms")

if st.button("Predict"):
    price = model.predict([[area, bed, bath]])
    st.success(f"Estimated Price: {price[0]}")
