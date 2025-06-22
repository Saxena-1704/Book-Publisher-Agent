```bash
# 📚 Book Publisher Agent

This project is an AI-powered content workflow tool that automates scraping, spinning, refining, and human reviewing of online chapter content (e.g., from Wikisource). It uses **Streamlit** for the user interface and **ChromaDB** for versioned storage.

---

## 🚀 How to Use

Follow these steps in order:

1️⃣ Run the App


streamlit run app.py

2️⃣ Scrape a Chapter
Stay on the Book Publisher Agent tab (the default home screen).

Paste the chapter URL (e.g., from Wikisource) into the input field.

Click "Scrape Chapter".

Once the raw text appears, click "Save to DB" to store it.

3️⃣ Spinner Page
From the left sidebar dropdown, switch to Spinner.

Click "Load Raw Content".

The AI will spin the content into a new version.

Save the spun version to the DB using the provided button.

4️⃣ Refiner Page
Switch to Refiner from the sidebar.

Load the spun version.

Click "Refine" to polish and clean the content.

Save the refined version to the DB.

5️⃣ Human Reviewer Page
Go to Human Reviewer from the sidebar.

Click "📂 Load Refined Content".

Edit the content if needed.

Click "💾 Save Reviewed Content".

Optionally, rate the version (0–5) and save it to the DB.

🧠 Tech Stack
Frontend/UI: Streamlit

Scraping: Playwright

LLM: Gemini (Google Generative AI)

Vector DB: ChromaDB

RL Feedback System: (Planned - user ratings to guide model selection)

