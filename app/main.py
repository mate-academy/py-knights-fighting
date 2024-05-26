import json
from typing import Dict
from app.battle import battle


def load_knights_config(filename: str) -> Dict[str, Dict]:
    with open(filename, "r") as file:
        return json.load(file)


knights_config = load_knights_config("../app/knights.json")

battle_results = battle(knights_config)
print(battle_results)
