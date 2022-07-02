import pickle
import time
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

svm_model = pickle.load(open('D:\coding\DiabetesPredictionML\svm_model.sav', 'rb'))
# knn_model = pickle.load(open('D:\coding\DiabetesPredictionML\knn_model.sav', 'rb'))
dtt_model = pickle.load(open('D:\coding\DiabetesPredictionML\dtt_model.sav', 'rb'))
# rf_model = pickle.load(open('D:\coding\DiabetesPredictionML\rf_model.sav', 'rb'))
# naive_bayes_model = pickle.load(open('D:\coding\DiabetesPredictionML\naive_bayes_model.sav', 'rb'))
# lr_model = pickle.load(open('D:\coding\DiabetesPredictionML\lr_model.sav', 'rb'))

# heart_disease_model = pickle.load(open('C:/Users/siddhardhan/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))

# parkinsons_model = pickle.load(open('C:/Users/siddhardhan/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav', 'rb'))

#Page Title
st.set_page_config(
   page_title="Diabetes Prediction",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
   
)

#  with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")


# sidebar for navigation
with st.sidebar:
   
    selected = option_menu('Select Type Of Algorithm:',
                          
                          ['Decision Tree',
                           'SVM',
                           'Naive Bayes',
                            'SVM',
                           'SVM',],
                          icons=['activity','heart','person'],
                          default_index=0)
   

# Diabetes Prediction Page

    
    # page title
st.title('Diabetes Prediction using ML')
col1, col2, col3 = st.columns([4,8,4])

with col1:
    st.write("")

with col2:
    st.image("https://miro.medium.com/max/1400/1*INSggrGiQ1lCgU8YTsfEVw.png")

with col3:
    st.write("")

    # getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
        
with col2:
    Glucose = st.text_input('Glucose Level')
    
with col3:
    BloodPressure = st.text_input('Blood Pressure value')
    
with col1:
    SkinThickness = st.text_input('Skin Thickness value')
    
with col2:
    Insulin = st.text_input('Insulin Level')
    
with col3:
    BMI = st.text_input('BMI value')
    
with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
with col2:
    Age = st.text_input('Age of the Person')
    
    
    # # code for Prediction
    # diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        if(selected == "Decision Tree"):
            
            dtt_prediction = dtt_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
            if (dtt_prediction[0] == 1):
                #  diab_diagnosis = 'The person is diabetic'
                 st.success('The person is diabetic')
            else:
                # diab_diagnosis = 'The person is not diabetic'
                st.error('The person is not diabetic')

        if(selected == "SVM"):
            
            svm_prediction = svm_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
            if (svm_prediction[0] == 1):
                #  diab_diagnosis = 'The person is diabetic'
                 st.success('The person is diabetic')
            else:
                # diab_diagnosis = 'The person is not diabetic'
                st.error('The person is not diabetic')
        



    
#     hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 