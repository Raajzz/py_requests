import requests

def get_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")