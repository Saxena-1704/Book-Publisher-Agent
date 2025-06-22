from db_handler import save_raw
from scraper import scrape_chapter
import streamlit as st
import subprocess
from datetime import datetime
from id_generator import generate_doc_id

st.set_page_config(page_title="Book Publisher Agent", layout="centered")
st.title("📚 Book Publisher Agent")
st.write("Enter the URL of the chapter you want to scrape and process:")

# URL input
url = st.text_input("🔗 Chapter URL", placeholder="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

# Input for document ID


# Global placeholder for content
content = ""

# Scrape Button
if st.button("Scrape Chapter"):
    if url.strip() == "":
        st.error("Please enter a valid URL.")
    else:
        with open("url_input.txt", "w") as f:
            f.write(url)
        st.success("✅ URL saved! Scraping now...")

        result = subprocess.run(["E:/book publisher agent/venv/Scripts/python.exe", "scraper.py"])

        if result.returncode == 0:
            st.success("✅ Scraping done!")
            with open("chapter1_raw.txt", "r", encoding="utf-8") as f:
                content = f.read()
                st.text_area("Scraped Content", content, height=300)
        else:
            st.error("❌ Error during scraping.")
version = "raw"
doc_id = generate_doc_id(url,version)
# Save to database
with open("chapter1_raw.txt","r") as f:
    content = f.read()
st.write("⭐ Rate this version (0 to 5):")
rating = st.slider("Rating", min_value=0, max_value=5, step=1)

if st.button("Submit Rating"):
    st.success(f"You rated this version: {rating}/5")
    # You can now use this `rating` variable wherever needed

if st.button("💾 Save to DB"):
    if content == "":
        st.error("No content to save. Please scrape first.")
    elif doc_id.strip() == "":
        st.error("Please enter a document ID.")
    else:
        metadata = {
            "version": "raw",
            "rating":rating,
            "source": url,
            "timestamp": datetime.now().isoformat(),
        }
        save_raw(content, metadata, doc_id)
        st.success(f"✅ Document '{doc_id}' saved to DB.")
