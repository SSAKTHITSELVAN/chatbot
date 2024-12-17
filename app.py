import streamlit as st

# Title
st.title("Minimal Streamlit App")

# Input Section
st.header("User Input")
name = st.text_input("What's your name?", "")

# Output Section
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!")
else:
    st.write("Please enter your name above.")
