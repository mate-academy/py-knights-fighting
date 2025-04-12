from typing import Dict


class Knight:
    def __init__(self, config: Dict[str, int]) -> None:
        self.name: str = config["name"]
        self.hp: int = config["hp"]
        self.power: int = config["power"]

    def take_damage(self, amount: int) -> None:
        self.hp -= amount
