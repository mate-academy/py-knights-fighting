class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.power: int = knight.get("power")
        self.hp: int = knight.get("hp")
        self.armour: list[dict] = knight.get("armour")
        self.weapon: dict = knight.get("weapon")
        self.potion: dict = knight.get("potion")
        self.protection = 0

    def prepare_to_battle(self) -> None:
        self.protection += sum(
            armour.get("protection")
            for armour in self.armour
        )
        self.power += self.weapon.get("power")
        self.parse_potion()

    def parse_potion(self) -> None:
        if self.potion:
            for key in self.potion["effect"]:
                self.__dict__[key] += self.potion["effect"][key]
