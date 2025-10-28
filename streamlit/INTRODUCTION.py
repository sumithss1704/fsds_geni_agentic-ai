import streamlit as st

st.title("Welcome to Streamlit!")

st.write("This app calculates the square of a number you provide.")

st.header("Input Section")
number=st.slider("Select a number", 0, 100, 25)

st.subheader("Your Selected Number")
squared_value = number ** 2
st.write(f"The square of {number} is {squared_value}.")
