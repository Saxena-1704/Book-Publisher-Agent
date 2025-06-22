from playwright.sync_api import sync_playwright

def scrape_chapter(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path="chapter1.png", full_page=True)

        content = page.inner_text("body")
        with open("chapter1_raw.txt", "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()
        return content

# ✅ Read the URL from file and call scrape_chapter
if __name__ == "__main__":
    with open("url_input.txt", "r") as file:
        url = file.read().strip()
        scrape_chapter(url)

