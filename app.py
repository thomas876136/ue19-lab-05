import requests

URL = "https://v2.jokeapi.dev/joke/Any?lang=en&type=single"

def get_joke():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("joke", "Pas de blague trouvée.")

if __name__ == "__main__":
    try:
        print(get_joke())
    except requests.RequestException as e:
        print(f"Erreur lors de l'appel à l'API : {e}")