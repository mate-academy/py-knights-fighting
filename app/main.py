from typing import Dict, Any

from app.knights_logic import create_knights, duels, tournament_result


def battle(knights: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    create_knights(knights)
    duels()
    return tournament_result()
