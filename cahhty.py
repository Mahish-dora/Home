import streamlit as st
# set the title of the app
st.title("Welcome to my First Streamlit APP")

#ADD a text_input
name = st.text_input("Enter your name:")

#Display the name entered by user
if name:
    st.write(f"hello, {name} Welcome to the app") 
    
