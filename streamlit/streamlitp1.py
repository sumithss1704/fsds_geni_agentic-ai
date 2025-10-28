import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("This app demonstrates basic Streamlit functionality.")

st.sidebar.header("Sidebar Input")
user_input = st.sidebar.text_input("Enter your name", "Shetti")

age = st.sidebar.slider("Enter your age", min_value=0, max_value=120, value=25)
fav_col=st.sidebar.selectbox("Select your favorite color", ["Red", "Green", "Blue", "Yellow"])

st.header("User Information")
st.write(f"you are {user_input}, {age} years old, and your favorite color is {fav_col}.")

st.subheader("Sample DataFrame")
data=pd.DataFrame(
    np.random.randn(10, 6),
    columns=['A', 'B', 'C','D','E','F']
)

st.dataframe(data)

if st.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())
if st.button("Click Me"):
    st.write("Button clicked! Hello, " + user_input + "!")
else:
    st.write("Click the button to see a greeting.") 