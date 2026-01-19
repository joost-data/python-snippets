import requests

def fetch_json(url, params=None, headers=None):
    """
    Fetch JSON data from a REST API.
    Returns parsed JSON or raises an error.
    """
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

