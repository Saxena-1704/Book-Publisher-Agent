import chromadb

# ✅ Create client with the new method
client = chromadb.PersistentClient(path="chroma_store")

# ✅ Create a collection
collection = client.get_or_create_collection(name="book_versions")

metadata = {
    "version": "refined",
    "source": "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1",
    "model": "gemini-1.5",
    "timestamp": "2025-06-14T18:30:00"
}
with open("chapter1_refined.txt","r",encoding="utf-8") as f:
    refined_text= f.read()

collection.add(
    documents=[refined_text],
    metadatas=[metadata],
    ids=["chapter1_refined_v1"]
)

def save_raw(text, metadata, doc_id):
    collection.add(documents=[text], metadatas=[metadata], ids=[doc_id])

def save_spun(text, metadata, doc_id):
    collection.add(documents=[text], metadatas=[metadata], ids=[doc_id])

def save_refined(text, metadata, doc_id):
    collection.add(documents=[text], metadatas=[metadata], ids=[doc_id])

def save_human(text, metadata, doc_id):
    collection.add(documents=[text], metadatas=[metadata], ids=[doc_id])

results = collection.get(ids=["chapter1_refined_v1"])
print(results["documents"][0])

results = collection.query(
    query_texts=["morning sunrise in Polynesia"],
    n_results=1
)


