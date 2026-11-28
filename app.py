import streamlit as st
import pandas as pd
from pathlib import Path

st.title("FIFA World Cup 2022")
st.header("Các cầu thủ ghi bàn")

df = pd.read_csv(Path(__file__).parent / "data.txt")

st.subheader("Bảng dữ liệu cầu thủ")
st.dataframe(df)

st.subheader("Dữ liệu định tính")
st.write(df["Nationality"].unique())

st.subheader("Dữ liệu định lượng")
st.write(df.describe())

st.subheader("Câu hỏi 1 - Định tính")
st.write("Các cầu thủ trong bộ dữ liệu mang những quốc tịch nào?")
st.write("Trả lời: Các cầu thủ đến từ các quốc gia sau:")
st.write(", ".join(df["Nationality"].dropna().unique()))

st.subheader("Câu hỏi 2 - Định lượng")
st.write("Số bàn thắng trung bình của các cầu thủ là bao nhiêu?")

average = df["Goals"].mean()
st.write(f"Trả lời: Số bàn thắng trung bình của mỗi cầu thủ là {average:.2f} bàn.".replace(".", ",", 1))