import requests
from bs4 import BeautifulSoup

def get_links(url):
    """
    Fetch all hyperlinks from a webpage.
    Returns a list of URLs.
    """
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)

    return links

