import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book Search", page_icon="📚")

st.title("📚 Book Search (Scraped via Scrapy)")

# Membaca data hasil Scrapy
df = pd.read_csv("books.csv")

keyword = st.text_input("Cari judul buku:")

if keyword:
    hasil = df[df["title"].str.contains(keyword, case=False, na=False)]
else:
    hasil = df

st.success(f"✨ Ditemukan {len(hasil)} hasil")

for _, row in hasil.iterrows():
    st.markdown(f"## [{row['title']}]({row['link']})")
    st.write(
        f"**Price:** {row['price']} | "
        f"**Rating:** {row['rating']} | "
        f"**Availability:** {row['availability']}"
    )
    st.divider()
