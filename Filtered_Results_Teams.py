import json
import sys
import os

TOURNAMENT_ID = sys.argv[1]

teams_file = f"Tournament.{TOURNAMENT_ID}.TeamResult.json"
brackets_file = f"Tournament.{TOURNAMENT_ID}.BracketsResult.json"
output_dir = "data_base"
output_file = f"Tournament.{TOURNAMENT_ID}.FinalResults.json"

os.makedirs(output_dir, exist_ok=True)


with open(teams_file, "r", encoding="utf-8") as f:
    teams_data = json.load(f)

with open(brackets_file, "r", encoding="utf-8") as f:
    brackets_data = json.load(f)

placements = {entry["tournamentTeamId"]: entry["placement"] for entry in brackets_data["standings"]}

filtered_teams = []
for team in teams_data:
    team_id = team["id"]
    if team["seed"] is not None:  
        filtered_team = {
            "team_id": team_id,
            "team_name": team["name"],
            "placement": placements.get(team_id, None),  
            "members": [
                {"name": member["name"], "discord_id": member["discordId"]}
                for member in team["members"]
            ]
        }
        filtered_teams.append(filtered_team)

output_path = os.path.join(output_dir, output_file)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(filtered_teams, f, indent=4, ensure_ascii=False)

print(f"Données enregistrées dans {output_dir}")

os.remove(teams_file)
os.remove(brackets_file)


print("Traitement terminé")
