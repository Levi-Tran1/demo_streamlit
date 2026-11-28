import streamlit as st
import pandas as pd
from pathlib import Path

st.title("FIFA World Cup 2022")
st.header("Top Strikers")

df = pd.read_csv(Path(__file__).parent / "data.txt")

st.subheader("Football Player Dataset")
st.dataframe(df)

st.subheader("Qualitative Data")
st.write(df["Nationality"].unique())

st.subheader("Quantitative Data")
st.write(df.describe())

st.subheader("Question 1 - Qualitative")
st.write("What are the nationalities of the players?")
st.write(df["Nationality"].unique())

st.subheader("Question 2 - Quantitative")
st.write("What is the average number of goals?")
st.write(df["Goals"].mean())