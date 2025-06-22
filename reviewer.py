import google.generativeai as genai
import os
genai.configure(api_key="AIzaSyBz7ZKN-wzd6vEmz3n0fZu1pWzPp09zAUU")

def review_chapter(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    prompt=f"""You are an expert reviewing agent. Check if there are any spelling or grammatical mistakes in the given text and generate the text again with the correction.\n\n{content}"""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    reviewed_text = response.text
    with open(output_file, "w",encoding="utf-8") as f:
        f.write(reviewed_text)
    print("Reviewed content saved to",output_file)

if __name__ == "__main__":
    review_chapter("chapter1_spun.txt","chapter1_reviewed.txt")