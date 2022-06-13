import streamlit as st
import requests as re
import numpy as np


def main():

    st.title("Spam Classification")
    gender = st.number_input("GENDER. Enter 1 for Male and O for Female")
    age = st.number_input("AGE")
    smoking = st.number_input("SMOKING")
    yellow_finger = st.number_input("YELLOW_FINGERS")
    anxiety = st.number_input("ANXIETY")
    peer = st.number_input("PEER_PRESSURE")
    chronic = st.number_input("CHRONIC_DISEASE")
    fatigue = st.number_input("FATIGUE")
    allergy = st.number_input("ALLERGY")
    wheezing = st.number_input("WHEEZING")
    alcohol =  st.number_input("ALCOHOL_CONSUMPTION")
    coughing = st.number_input("COUGHING")
    breath = st.number_input("SHORTNESS_OF_BREATH")
    swallow =  st.number_input("SWALLOWING_DIFFICULTY")
    chest =  st.number_input("CHEST_PAIN")
   
    features = np.array([[gender, age, smoking, yellow_finger, anxiety, peer, chronic, fatigue, allergy, wheezing, alcohol, coughing, breath, swallow, chest]])
    if st.button('Predict'):
        values =  {
    "GENDER": gender,
    "AGE": age,
    "SMOKING": smoking,
    "YELLOW_FINGERS": yellow_finger,
    "ANXIETY": anxiety,
    "PEER_PRESSURE": peer,
    "CHRONIC_DISEASE": chronic,
    "FATIGUE": fatigue,
    "ALLERGY": allergy,
    "WHEEZING": wheezing,
    "ALCOHOL_CONSUMPTION": alcohol,
    "COUGHING": coughing,
    "SHORTNESS_OF_BREATH": breath,
    "SWALLOWING_DIFFICULTY": swallow,
    "CHEST_PAIN": chest
    }
        res = re.post(f"https://lung-cancer-prediction-api.herokuapp.com/predict/",json=values)
        with st.spinner('Classifying, please wait....'):
            st.write(res.json())

if __name__ == '__main__':
    main()