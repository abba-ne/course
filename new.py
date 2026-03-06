import pandas as pd
import streamlit as st
import joblib

model = joblib.load("new.pkl")
encoder = joblib.load("encoder.pkl")

print(model)

st.title("course recommendation sysytem")

computer_knowledge = st.selectbox("computer_knowledge: ", ['basic','pro'])
age = st.slider("age: ", 18, 100)
device = st.selectbox("device: ", ['pc', 'phone'])


if st.button("submit"):
    data = pd.DataFrame({
        "computer_knowledge": [computer_knowledge],
        "age": [age],
        "device": [device]
        })
    data['computer_knowledge'] = data['computer_knowledge'].str.lower
    data['device'] = data['device'].str.lower

    encoded_data = encoder.transform(data)
    prediction =  model.predict(encoded_data)
    predicted = prediction[0]
    st.success(f"Recommendation course: {predicted}")
    

print(2)