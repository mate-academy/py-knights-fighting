from __future__ import annotations


class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0
        self.prepare_for_battle(knight_config)

    def prepare_for_battle(self, knight_config: dict) -> None:
        if knight_config["armour"]:
            for armor in knight_config["armour"]:
                self.protection += armor["protection"]
        self.power += knight_config["weapon"]["power"]
        if knight_config["potion"]:
            if "power" in knight_config["potion"]["effect"]:
                self.power += knight_config["potion"]["effect"]["power"]

            if "protection" in knight_config["potion"]["effect"]:
                self.protection \
                    += knight_config["potion"]["effect"]["protection"]

            if "hp" in knight_config["potion"]["effect"]:
                self.hp += knight_config["potion"]["effect"]["hp"]

    def fight_with(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection
        if self.hp < 0:
            self.hp = 0
        if opponent.hp < 0:
            opponent.hp = 0
