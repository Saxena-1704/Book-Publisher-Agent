from reviewer import review_chapter
import streamlit as st
import os
from db_handler import save_refined
from id_generator import generate_doc_id
from app import url
from datetime import datetime

st.set_page_config(page_title="Refiner", layout="centered")
st.title("Refiner")
st.write("Click the button below to load the spun content.")


content ="" 

if st.button("Load spun content"):
    if os.path.exists("chapter1_spun.txt"):
        with open("chapter1_spun.txt","r",encoding="utf-8") as f:
            content = f.read()
    else:
        st.error("'chapter1_spun.txt'not found")

st.text_area("Spun content",content,height=200,disabled=True)   
if st.button("Refine content"):
    if os.path.exists("chapter1_raw.txt"):
        review_chapter("chapter1_spun.txt", "chapter1_refined.txt")
        st.success("✅ Content spun successfully and saved to 'chapter1_spun.txt'.")
    else:
        st.error("❌ Cannot spin. 'chapter1_raw.txt' not found.")  
version = "refined"
if st.button("Rate the refined content"):
    if os.path.exists("chapter1_refined.txt"):
        
            with open("chapter1_refined.txt","r") as f:
                content = f.read()
                st.text_area(content,disabled=True)

st.write("⭐ Rate this version (0 to 5):")
rating = st.slider("Rating", min_value=0, max_value=5, step=1)
if st.button("Submit Rating"):
        st.success(f"You rated this version: {rating}/5")
        
doc_id = generate_doc_id(version,url)
if st.button("💾 Save to DB"):
    file = open("chapter1_refined.txt","r")
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
        save_refined(content, metadata, doc_id)
        st.success(f"✅ Document '{doc_id}' saved to DB.")