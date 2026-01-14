from __future__ import annotations


class Knight:
    def __init__(self, knights_config: dict) -> None:
        self.name = knights_config["name"]
        self.protection = 0
        self.hp = knights_config["hp"]
        for poram in knights_config["armour"]:
            self.protection += poram["protection"]
        self.power = knights_config["weapon"]["power"] + knights_config["power"]
        if knights_config["potion"] is not None:
            if "power" in knights_config["potion"]["effect"]:
                self.power += knights_config["potion"]["effect"]["power"]

            if "protection" in knights_config["potion"]["effect"]:
                self.protection += knights_config["potion"]["effect"]["protection"]

            if "hp" in knights_config["potion"]["effect"]:
                self.hp += knights_config["potion"]["effect"]["hp"]

    @staticmethod
    def battle(knight_one: Knight, knight_two: Knight) -> None:
        knight_one.hp -= knight_two.power - knight_one.protection
        knight_two.hp -= knight_one.power - knight_two.protection
        if knight_one.hp <= 0:
            knight_one.hp = 0

        if knight_two.hp <= 0:
            knight_two.hp = 0
