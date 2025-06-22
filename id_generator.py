import re
from urllib.parse import urlparse

def generate_doc_id(url, version):
    parsed = urlparse(url)
    source = parsed.netloc.split('.')[0]  # e.g., 'en' → 'wikisource'
    path = parsed.path.replace("/wiki/", "").replace("/", "_").lower()
    path = re.sub(r'[^a-z0-9_]', '', path)  # clean any weird chars
    return f"{source}__{path}__{version}"
