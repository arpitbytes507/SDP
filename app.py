import streamlit as st
import numpy as np 
import pandas as pd 

st.title("My first Steamlist app")
st.write("streamlit: Hi Arpit")
st.text("Start")

name = st.text_input("Enter Name")
if st.button("Greet"):
    st.success(f"Hiii, {name}")

df = pd.DataFrame(np.random.randn(10,2), columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("NAvigation")
st.image("https://wpengine.com/resources/optimize-images-for-web/")
st.video("https://www.youtube.com/watch?v=zo78v8YS7IA")

upload_file = st.file_uploader("Upload a csv", type='csv')
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

st.code("for i in range(2): print(i)", language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("ase"):
    st.write("write")

with st.form("login form"):
    username = st.text_input("username")
    passowrd = st.text_input("Password", type="password")
    submitted = st.form_submit_button("login")

if submitted:
    st.success(f"Welocm")

import matplotlib.pyplot as plt

fig, ax = plt.subplot()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)