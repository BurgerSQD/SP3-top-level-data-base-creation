
import json
import sys
import requests

def save_json_to_file(data, tournament_id):
    """Enregistre un dictionnaire en JSON dans un fichier avec un nom spécifique."""
    filename = f"Tournament.{tournament_id}.TeamResult.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Données enregistrées dans {filename}")

TOURNAMENT_ID = sys.argv[1]
TOKEN = sys.argv[2]
API_URL = f"https://sendou.ink/api/tournament/{TOURNAMENT_ID}/teams"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    save_json_to_file(data, TOURNAMENT_ID)  # Enregistrement des données
else:
    print(f"Erreur {response.status_code}: Impossible de récupérer les teams")
