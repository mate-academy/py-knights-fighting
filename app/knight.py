# app/models.py

class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.armour = data["armour"]
        self.weapon = data["weapon"]
        self.potion = data["potion"]
        self.protection = 0

    def prepare_for_battle(self) -> None:
        for piece in self.armour:
            self.protection += piece["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            effect = self.potion["effect"]
            if "hp" in effect:
                self.hp += effect["hp"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]

    def take_damage(self, damage_points: int) -> None:
        self.hp -= (damage_points - self.protection)
        if self.hp < 0:
            self.hp = 0
