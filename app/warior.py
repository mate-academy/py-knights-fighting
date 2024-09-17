class Warior:
    def __init__(self, warior: dict) -> None:
        self.name = warior["name"]
        self.power = warior["power"] + warior["weapon"]["power"]
        self.hp = warior["hp"]
        self.protection = self.calculate_protection(warior["armour"])

        self.boost_effects(warior["potion"])

    def calculate_protection(self, armour: list) -> int:
        if len(armour) == 0:
            return 0

        return sum([armour_part["protection"] for armour_part in armour])

    def boost_effects(self, potion: dict) -> None:
        if potion is None:
            return

        effect = potion["effect"]

        power = effect.get("power", 0)
        hp = effect.get("hp", 0)
        protection = effect.get("protection", 0)

        self.power += power
        self.hp += hp
        self.protection += protection
