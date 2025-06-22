import streamlit as st
import os
from db_handler import save_human
from id_generator import generate_doc_id
from app import url
from datetime import datetime

st.set_page_config(page_title="Human Reviewer", layout="centered")
st.title("Human Reviewer")
st.write("Click the button below to load the refined the content")

content = ""

if st.button("📂 Load Refined Content"):
    if os.path.exists("chapter1_refined.txt"):
        with open("chapter1_refined.txt", "r", encoding="utf-8") as f:
            original_content = f.read()

        # Show editable area and get user input
        if "edited_content" not in st.session_state:
            st.session_state.edited_content = original_content

        st.session_state.edited_content = st.text_area(
            "✏️ Edit the Content if required", 
            value=st.session_state.edited_content, 
            height=200
        )

        if st.button("💾 Save Reviewed Content"):
            with open("chapter1_reviewed.txt", "w", encoding="utf-8") as f:
                f.write(st.session_state.edited_content)
            st.success("✅ Reviewed content saved!")

    else:
        st.error("❌ Refined file not found.")


version = "human_reviewed"

if st.button("Rate the content"):
    if "edited_content" in st.session_state:
        content = st.session_state.edited_content
    elif os.path.exists("chapter1_reviewed.txt"):
        with open("chapter1_reviewed.txt", "r") as f:
            content = f.read()
    else:
        content = "❌ No reviewed content found."

    st.text_area("📝 Reviewed Content", value=content, height=200, disabled=True)

st.write("⭐ Rate this version (0 to 5):")
rating = st.slider("Rating", min_value=0, max_value=5, step=1)
if st.button("Submit Rating"):
        st.success(f"You rated this version: {rating}/5")

doc_id = generate_doc_id(version,url)
if st.button("💾 Save to DB"):
    file = open("chapter1_reviewed.txt","r")
    content=file.read()
    if content == "":
        st.error("No content to save. Please spin content first.")
    elif doc_id.strip() == "":
        st.error("Please enter a document ID.")
    else:
        metadata = {
            "version": "Human reviewed",
            "rating":rating,
            "source": url,
            "timestamp": datetime.now().isoformat(),
        }
        save_human(content, metadata, doc_id)
        st.success(f"✅ Document '{doc_id}' saved to DB.")

