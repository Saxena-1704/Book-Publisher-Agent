from spinner import spin_chapter
import streamlit as st
import os
from app import url
from id_generator import generate_doc_id
from db_handler import save_spun
from datetime import datetime

st.set_page_config(page_title="Spinner", layout="centered")
st.title("🌀 Spinner")
st.write("Click the button below to load the raw content.")

# Initialize content to empty string
content = ""

if st.button("📂 Load Raw Content"):
    if os.path.exists("chapter1_raw.txt"):
        with open("chapter1_raw.txt", "r", encoding="utf-8") as f:
            content = f.read()
    else:
        st.error("❌ 'chapter1_raw.txt' not found.")

st.text_area("📜 Raw Content", content, height=200, disabled=True)
version = "spun"
st.write("Click the button to spin the content into a new version.")
if st.button("✨ Spin Content"):
    if os.path.exists("chapter1_raw.txt"):
        spin_chapter("chapter1_raw.txt", "chapter1_spun.txt")
        st.success("✅ Content spun successfully and saved to 'chapter1_spun.txt'.")
    else:
        st.error("❌ Cannot spin. 'chapter1_raw.txt' not found.")
if st.button("Rate the spun content"):
    if os.path.exists("chapter1_spun.txt"):
        
            with open("chapter1_raw.txt","r") as f:
                content = f.read()
                st.text_area(content,disabled=True)


st.write("⭐ Rate this version (0 to 5):")
rating = st.slider("Rating", min_value=0, max_value=5, step=1)
if st.button("Submit Rating"):
        st.success(f"You rated this version: {rating}/5") 

           
doc_id = generate_doc_id(version,url)
if st.button("💾 Save to DB"):
    file = open("chapter1_spun.txt","r")
    content=file.read()
    if content == "":
        st.error("No content to save. Please spin content first.")
    elif doc_id.strip() == "":
        st.error("Please enter a document ID.")
    else:
        metadata = {
            "version": "spun",
            "rating":rating,
            "source": url,
            "timestamp": datetime.now().isoformat(),
        }
        save_spun(content, metadata, doc_id)
        st.success(f"✅ Document '{doc_id}' saved to DB.")