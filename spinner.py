import google.generativeai as genai
import os

# Set your API key
genai.configure(api_key="AIzaSyBz7ZKN-wzd6vEmz3n0fZu1pWzPp09zAUU")  # Replace or use os.environ["GOOGLE_API_KEY"]

def spin_chapter(input_file, output_file):
    # Load chapter text
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Prompt Gemini to rewrite it
    prompt = f"""You are an expert book spinner. Rewrite the following chapter in a more modern, engaging, and vivid storytelling style. Do not change the meaning or structure too much, just improve its flow and language.\n\n{content}"""

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    spun_text = response.text

    # Save output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(spun_text)

    print("Spun content saved to", output_file)

#if __name__ == "__main__":
    #spin_chapter("chapter1_raw.txt", "chapter1_spun.txt")
