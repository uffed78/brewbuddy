import requests
from bs4 import BeautifulSoup

def fetch_bjcp_styles():
    """
    Skrapar och strukturerar BJCP-stilar från den officiella webbplatsen.
    """
    url = "https://www.bjcp.org/beer-styles/beer-style-guidelines/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    styles = {}
    for category in soup.select(".styleCategory"):
        category_name = category.find("h3").text.strip()
        styles[category_name] = []
        for style in category.select(".styleSubcategory"):
            style_name = style.find("h4").text.strip()
            styles[category_name].append(style_name)
    return styles
