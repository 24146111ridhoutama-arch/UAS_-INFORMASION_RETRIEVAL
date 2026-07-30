import streamlit as st
import json
import os

DATA_PATH = "data/books.json"

st.set_page_config(page_title="Book Crawler Search", layout="wide")
st.title("📚 Book Search (Scraped via Scrapy)")

# Load data
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.warning("Data belum tersedia. Menampilkan contoh atau pastikan file JSON ada.")
    data = []

# Input pencarian
query = st.text_input("Cari judul buku:", "")

# Filter data
if query:
    filtered = [item for item in data if query.lower() in item.get("title", "").lower()]
    st.markdown(f"### ✨ Ditemukan {len(filtered)} hasil")
else:
    filtered = data
    st.markdown(f"### ✨ Ditemukan {len(filtered)} hasil")

# Tampilkan hasil
for item in filtered:
    title = item.get('title', 'Tanpa Judul')
    price = item.get('price', '-')
    rating = item.get('rating', '-')
    availability = item.get('availability', '-')
    link = item.get('link', '#')
    
    st.markdown(f"### [{title}]({link})")
    st.markdown(f"**Price:** {price} | **Rating:** {rating} | **Availability:** {availability}")
    st.markdown("---")
