class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: str,
                 weapon: str, potion: str):
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.protection = self.calculate_protection()
        self.power = self.calculate_power()

    def calculate_protection(self):
        protection = sum(a["protection"] for a in self.armour)
        if self.potion and "protection" in self.potion.get("effect", {}):
            protection += self.potion["effect"]["protection"]
        return protection

    def calculate_power(self):
        power = self.base_power + (self.weapon["power"] if self.weapon else 0)
        if self.potion and "power" in self.potion.get("effect", {}):
            power += self.potion["effect"]["power"]
        return power

    def apply_potion(self) -> None:
        if self.potion and "hp" in self.potion.get("effect", {}):
            self.hp += self.potion["effect"]["hp"]

    def take_damage(self, opponent_power: int) -> None:
        damage = max(0, opponent_power - self.protection)
        self.hp = max(0, self.hp - damage)


def battle(knights_config: dict) -> None:
    knights = {
        key: Knight(
            name=value["name"],
            power=value["power"],
            hp=value["hp"],
            armour=value.get("armour", []),
            weapon=value.get("weapon"),
            potion=value.get("potion"),
        )
        for key, value in knights_config.items()
    }

    # Apply potions to all knights
    for knight in knights.values():
        knight.apply_potion()

    # Battles
    lancelot, mordred = knights["lancelot"], knights["mordred"]
    arthur, red_knight = knights["arthur"], knights["red_knight"]

    # Lancelot vs Mordred
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # Arthur vs Red Knight
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # Return battle results
    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {"name": "Berserk",
                   "effect": {"power": +15, "hp": -5, "protection": +10}},
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing", "effect": {"hp": +10, "power": +5}},
    },
}

print(battle(KNIGHTS))
