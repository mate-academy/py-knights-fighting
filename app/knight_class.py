from __future__ import annotations


class Knight:

    def __init__(self, parameters: dict) -> None:
        self.name = parameters.get("name")
        self.power = parameters.get("power")
        self.hp = parameters.get("hp")
        self.armour = parameters.get("armour")
        self.weapon = parameters.get("weapon")
        self.potion = parameters.get("potion")
        self.protection = 0
        self.ready_for_battle()

    def use_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def use_weapon(self) -> None:
        self.power += self.weapon["power"]

    def use_armour(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]

    def ready_for_battle(self) -> None:
        self.use_armour()
        self.use_weapon()
        self.use_potion()

    def take_damage(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        if self.hp <= 0:
            self.hp = 0

    def get_health(self) -> dict:
        return {self.name: self.hp}

    @staticmethod
    def return_result(*args) -> dict:
        result = {}
        for part in args:
            result.update(part.get_health())
        return result
