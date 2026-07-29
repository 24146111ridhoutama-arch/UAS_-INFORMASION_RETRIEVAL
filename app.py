import streamlit as st
import pandas as pd

st.set_page_config(page_title="UAS Information Retrieval")

st.title("📚 UAS Information Retrieval")
st.write("Nama : Ridho Utama")
st.write("NIM : 24146111")

# Membaca data otomatis dari GitHub
df = pd.read_csv("data.csv")

st.subheader("Data Buku")
st.dataframe(df)

keyword = st.text_input("Cari Judul atau Kategori")

if keyword:
    hasil = df[df.astype(str).apply(
        lambda x: x.str.contains(keyword, case=False)
    ).any(axis=1)]

    st.subheader("Hasil Pencarian")
    st.dataframe(hasil)
