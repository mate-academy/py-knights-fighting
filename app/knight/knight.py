from app.main import knights


class Knight:
    knights = dict()

    def __init__(self, name: str, power: int, hp: int, weapon: dict) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = weapon["name"]
        Knight.knights[name] = self

    def knight_armour(self, armours: list[dict]) -> None:
        for armour in armours:
            self.armour.append(armour["part"])
            self.protection += armour["protection"]

    def knight_potion(self, potion: dict) -> None:
        self.potion = potion["name"]
        for effect, value in potion["effect"].items():
            if effect == "power":
                self.power += value
            elif effect == "hp":
                self.hp += value
            elif effect == "protection":
                self.protection += value


for knight in knights.values():
    Knight(knight["name"], knight["power"], knight["hp"], knight["weapon"])
    if len(knight["armour"]) != 0:
        Knight.knight_armour(Knight.knights[knight["name"]], knight["armour"])
    if knight.get("potion"):
        Knight.knight_potion(Knight.knights[knight["name"]], knight["potion"])
print(Knight.knights)
print(Knight.knights["Mordred"].protection)
