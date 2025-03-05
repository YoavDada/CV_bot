import requests
from bs4 import BeautifulSoup

def get_content(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=headers)

    if page.status_code != 200:
        return "Failed to get content"

    soup = BeautifulSoup(page.text, 'html.parser') 

    elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'div'])

    skills_texts = []
    extracting = False 

    # Iterate through elements
    for element in elements:
        if extracting:
            # Stop if we hit another header
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] and extracting:
                break
            # Collect all subsequent <p> elements
            if element.name in ['p', 'ul'] and element.text.strip():
                skills_texts.append(element.text.strip())

        # Detect a header or paragraph containing "Skills"
        if "skills" in element.text.lower():
            extracting = True  # Start collecting from the next element

    # Print or return the extracted skills section
    return "\n".join(skills_texts) if skills_texts else "No 'Skills' section found."
