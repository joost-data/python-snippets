import requests
from bs4 import BeautifulSoup

def scrape_first_table(url):
    """
    Scrape the first HTML table on a webpage.
    Returns table rows as a list of lists.
    """
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    rows = []
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        if cols:
            rows.append([col.get_text(strip=True) for col in cols])

    return rows

