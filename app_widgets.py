import streamlit as st
import pandas as pd

# Add title
st.title("Streamlit Text Input")

# Get a user input
name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}")
# Get a user input based on a slider
age=st.slider("Select your age:",0,100,25)
if age:
    st.write(f"Your age is, {age}")
# Create a dropdown select box
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
if choice:
    st.write(f"You selected {choice}.")


# Create a csv file for demonstration
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

# Ask user to upload a csv file
uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    
# Display Data
st.dataframe(df)
st.table(df.iloc[0:2])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")

# Display interactive widgets
st.button('Hit me')
st.data_editor(df)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.camera_input("Camera Input")
st.color_picker('Pick a color')
