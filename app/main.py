# app/main/knight.py
class Knight:
    def __init__(self, config):
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")
        self.protection = 0

    def apply_armour(self):
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion is not None:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage):
        self.hp -= max(0, damage - self.protection)

    def is_alive(self):
        return self.hp > 0


# app/main.py
from app.main.knight import Knight


def battle(knights_config):
    knights = {name: Knight(config) for name, config in knights_config.items()}

    for knight in knights.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    # 1 Lancelot vs Mordred:
    knights["lancelot"].take_damage(knights["mordred"].power)
    knights["mordred"].take_damage(knights["lancelot"].power)

    # 2 Arthur vs Red Knight:
    knights["arthur"].take_damage(knights["red_knight"].power)
    knights["red_knight"].take_damage(knights["arthur"].power)

    # Return battle results:
    return {knight.name: knight.hp for knight in knights.values() if knight.is_alive()}
