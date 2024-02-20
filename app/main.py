from __future__ import annotations
from app.knights import KNIGHTS


class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.armour = data["armour"]
        self.protection = 0
        self.weapon = data["weapon"]
        self.potion = data.get("potion")

    def apply_armour(self) -> None:
        self.protection = sum(element["protection"] for element in self.armour)

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def check_fell(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def results_hp(self, other_knight: Knight) -> None:
        self.hp -= other_knight.power - self.protection
        other_knight.hp -= self.power - other_knight.protection

    def battle_pre(self, other_knight: Knight) -> None:
        for instance in (self, other_knight):
            # BATTLE PREPARATIONS:
            instance.apply_armour()
            instance.apply_weapon()
            instance.apply_potion_if_exist()

        # BATTLE:
        self.results_hp(other_knight)
        self.check_fell()
        other_knight.check_fell()

    def __str__(self) -> str:
        return f"{self.name}: {self.hp}"


def battle(knights_config: dict) -> dict:
    knights = {name: Knight(data) for name, data in knights_config.items()}

    lancelot = knights.get("lancelot")
    mordred = knights.get("mordred")
    arthur = knights.get("arthur")
    red_knight = knights.get("red_knight")

    if lancelot and mordred:
        lancelot.battle_pre(mordred)

    if arthur and red_knight:
        arthur.battle_pre(red_knight)

    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
