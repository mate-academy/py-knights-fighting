from __future__ import annotations


class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name: str = knight_config["name"]
        self.power: int = knight_config["power"]
        self.hp: int = knight_config["hp"]
        self.protection: int = 0
        self.prepare_for_battle(knight_config)

    def prepare_for_battle(self, knight_config: dict) -> None:
        armour = knight_config.get("armour", [])
        if armour:
            for armor in knight_config["armour"]:
                self.protection += armor["protection"]
        # According to the rules, each knight !must! have exactly !one! weapon
        # Because knights cannot fight an unarmed opponent
        self.power += knight_config["weapon"]["power"]
        # There is no need to check if weapon exist
        potion = knight_config.get("potion")
        if potion is not None:
            effect: dict = knight_config["potion"].get("effect", {})
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]

    def fight_with(self, opponent: Knight) -> None:
        self.hp -= max(0, opponent.power - self.protection)
        opponent.hp -= max(0, self.power - opponent.protection)
        if self.hp < 0:
            self.hp = 0
        if opponent.hp < 0:
            opponent.hp = 0
