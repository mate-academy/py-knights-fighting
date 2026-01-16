class Knights:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        for elem in self.armour:
            self.protection += getattr(
                Knights, "protection", elem["protection"]
            )
        self.battle_preparation()

    def __str__(self) -> str:
        return f"name = {self.name}, power = {self.power}, hp = {self.hp}"

    def battle_preparation(self) -> None:
        self.power += self.weapon["power"]
        if self.potion is not None:
            effects = self.potion["effect"]
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)
