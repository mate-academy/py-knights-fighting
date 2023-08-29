class AllKnights:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = None
        self.weapon = {}
        self.potion = None

    def apply_armour(self, total_armour=0) -> None:
        for a in self.armour:
            total_armour += a.protection
        if "protection" in self.potion["effect"]:
            total_armour += self.potion["effect"]["protection"]
        self.armour = total_armour

    def apply_weapon(self) -> None:
        total_power = self.weapon["power"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                total_power += self.potion["effect"]["power"]
        self.power = total_power

    def apply_hp(self) -> None:
        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


# create Lancelot
lancelot = AllKnights(name="Lancelot", power=35, hp=100)
lancelot.weapon = {"name": "Metal Sword", "power": 50}

# create Arthur
arthur = AllKnights(name="Arthur", power=45, hp=75)
arthur.armour = [Armour("helmet", 15), Armour("breastplate", 20), Armour("boots", 10)]
arthur.weapon = {"name": "Two-handed Sword", "power": 55}

# create Mordred
mordred = AllKnights(name="Mordred", power=30, hp=90)
mordred.armour = [Armour("breastplate", 15), Armour("boots", 10)]
mordred.weapon = {"name": "Poisoned Sword", "power": 60}
mordred.potion = {
    "name": "Berserk",
    "effect": {"power": +15, "hp": -5, "protection": +10}
}

# create Red_knight
red_knight = AllKnights(name="Red Knight", power=40, hp=70)
red_knight.armour = [Armour("breastplate", 25)]
red_knight.weapon = {"name": "Sword", "power": 45}
red_knight.potion = {
    "name": "Blessing",
    "effect": {"hp": +10, "power": +5}
}

warriors = [lancelot, arthur, mordred, red_knight]
for char in warriors:
    char.apply_armour()
    char.apply_weapon()
    char.apply_hp()

    # -------------------------------------------------------------------------------


def battle() -> set:
    lancelot.hp -= mordred.power - lancelot.armour
    mordred.hp -= lancelot.power - mordred.armour

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.armour
    red_knight.hp -= arthur.power - red_knight.armour

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.hp,
        arthur.hp,
        mordred.hp,
        red_knight.hp
    }


print(battle())
