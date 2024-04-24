# import streamlit as st
# from recommendation import recommend_doctors

# def main():
#     st.title('Doctor Recommendation System')

#     # User input
#     symptoms = st.multiselect('Select Symptoms:', ['Chest pain', 'Shortness of breath', 'Dizziness', 'Irregular heartbeat',
#                                                     'Swelling in legs or ankles', 'Rash', 'Itching', 'Dry skin', 'Acne',
#                                                     'Skin discoloration', 'Fatigue', 'Weight changes', 'Excessive thirst',
#                                                     'Frequent urination', 'Hair loss', 'Abdominal pain', 'Nausea', 'Vomiting',
#                                                     'Indigestion', 'Bloating', 'Headache', 'Numbness or tingling', 'Seizures',
#                                                     'Memory loss', 'Unexplained weight loss', 'Persistent cough',
#                                                     'Changes in bowel habits', 'Lumps or swelling', 'Fever', 'Cough',
#                                                     'Runny nose', 'Earache', 'Diarrhea', 'Depression', 'Anxiety', 'Insomnia',
#                                                     'Mood swings', 'Hallucinations', 'Pain or burning during urination',
#                                                     'Blood in urine', 'Lower back pain', 'Erectile dysfunction'])
#     age = st.number_input('Enter Your Age:', min_value=0, max_value=120, step=1)
#     sex = st.radio('Select Your Sex:', ['Male', 'Female'])
#     location = st.selectbox('Select Your Location:', ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata',
#                                                       'Hyderabad', 'Ahmedabad', 'Pune', 'Surat', 'Jaipur'])

#     # Recommendation
#     st.subheader('Top Doctors Recommended:')
#     doctors_df = recommend_doctors(symptoms, age, sex, location)
#     st.dataframe(doctors_df)

# if __name__ == '__main__':
#     main()


import pandas as pd
import streamlit as st
from recommendation import recommend_doctors

def main():
    st.title('Doctor Recommendation System')

    # User input
    symptoms = st.text_area('Enter Symptoms (separated by commas):')
    symptoms = [s.strip() for s in symptoms.split(',')]
    age = st.number_input('Enter Your Age:', min_value=0, max_value=120, step=1)
    # sex = st.radio('Select Your Sex:', ['Male', 'Female'])
    location = st.selectbox('Select Your Location:', ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata',
                                                      'Hyderabad', 'Ahmedabad', 'Pune', 'Surat', 'Jaipur'])

    # Recommendation
    st.subheader('Top Doctors Recommended:')
    doctors_df = recommend_doctors(symptoms, age, location)
    st.dataframe(doctors_df)

if __name__ == '__main__':
    main()

