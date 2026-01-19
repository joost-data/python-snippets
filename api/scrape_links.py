import requests
from bs4 import BeautifulSoup
import csv


def scrape_languages_and_salaries(url):
    """
    Download a webpage, create a soup object,
    scrape language names and annual average salaries,
    and return the data.
    """

    # 1. Download the webpage
    html = requests.get(url).text

    # 2. Create BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

    # 3. Scrape language names and salaries
    results = []

    for row in soup.select("tr")[1:]:  # skip header row
        cells = row.find_all("td")
        if len(cells) < 2:
            continue

        results.append({
            "language": cells[0].get_text(strip=True),
            "average_salary": cells[1].get_text(strip=True)
        })

    return results


def save_to_csv(data, filename):
    """
    Save scraped data to a CSV file.
    """

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["language", "average_salary"])

        for item in data:
            writer.writerow([item["language"], item["average_salary"]])


# -------------------------
# Script execution
# -------------------------

URL = "INSERT URL HERE"
OUTPUT_FILE = "INSERT_FILENAME.csv"

languages_and_salaries = scrape_languages_and_salaries(URL)
save_to_csv(languages_and_salaries, OUTPUT_FILE)
