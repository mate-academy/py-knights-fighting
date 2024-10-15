from typing import Dict, Any


class Armour:
    def __init__(self, armour_data: Dict[str, Any]) -> None:
        self.protection = sum(part["protection"] for part in armour_data)
