import streamlit as st
import requests
import json
import pandas as pd

#functions
import requests
import json
def get_prediction(data={"A":499.5,"B":499.5,"C":499.5,"D":499.5}):
  url = 'https://askai.aiclub.world/2520283e-93a6-490a-83bd-2e1fa5b388b3'#copy your URL here 
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  response = json.loads(response)['body']
  response = json.loads(response)['predicted_label']
  return response

#reading the dataframe
data = pd.read_csv('averages_project_3.csv')

#title for the web app
st.title("Average AI")

#we will  use a select box to navigate through datasets and predictions
navigation = st.selectbox("Select any option", ['Dataset','Prediction Dashboard'])

if navigation == "Dataset":
    st.header(navigation)
    #setting the dataset
    st.dataframe(data)

if navigation == "Prediction Dashboard":
    st.title(navigation)

    A = st.slider("Number1", 0.00, 999.00, 100.00)
    B = st.slider("Number 2", 0.00, 999.00, 100.00)
    C = st.slider("Number 3", 0.00, 999.00, 100.00)
    D = st.slider("Number 4", 0.00, 999.00, 100.00)

    input_dict = {
        "A" : A,
        "B" : B,
        "C" : C,
        "D" : D
    }

    predictions = get_prediction(input_dict)
    st.subheader("Average: {}".format(predictions))
    
    #setting up the user input dashboard
   
