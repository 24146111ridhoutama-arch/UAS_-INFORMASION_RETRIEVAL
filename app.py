import streamlit as st
import pandas as pd

st.set_page_config(page_title="Information Retrieval", layout="wide")

st.title("📚 UAS Information Retrieval")
st.write("Nama : Ridho Utama")
st.write("Mata Kuliah : Information Retrieval")

uploaded_file = st.file_uploader("Upload File CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data")
    st.dataframe(df)

    keyword = st.text_input("Cari Data")

    if keyword:
        hasil = df[df.astype(str).apply(lambda x: x.str.contains(keyword, case=False)).any(axis=1)]

        st.subheader("Hasil Pencarian")
        st.dataframe(hasil)
else:
    st.info("Silakan upload file CSV.")
