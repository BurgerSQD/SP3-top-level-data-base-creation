import requests
import subprocess

tonken_api = input("Entrez l'API KEY: ")
tournament_ids = input("Entrez les Tournament IDs séparés par des espaces : ").split()


# Exécuter chaque script en leur passant les Tournament IDs
for tournament_id in tournament_ids:
    subprocess.run(["python", "Teams_requests_final.py", str(tournament_id), str(tonken_api)])
    subprocess.run(["python", "Brackets_result_requests_final.py", str(tournament_id), str(tonken_api)])
    subprocess.run(["python", "Filtered_Results_Teams.py", str(tournament_id), str(tonken_api)])
