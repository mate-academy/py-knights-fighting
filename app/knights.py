class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list = None, weapon: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour if armour is not None else []
        self.weapon = weapon if weapon is not None else {}
        self.potion = potion
        self.total_protection = 0

    def add_protection(self) -> int:
        if self.armour:
            for member in self.armour:
                if "protection" in member:
                    self.total_protection += member["protection"]
        if self.potion and isinstance(self.potion, dict):
            effect = self.potion.get("effect")
            if isinstance(effect, dict):
                self.total_protection += effect.get("protection", 0)
        return self.total_protection

    def add_power(self) -> int:
        if self.weapon is not None:
            self.power += self.weapon["power"]
        if self.potion and isinstance(self.potion, dict):
            effect = self.potion.get("effect")
            if isinstance(effect, dict):
                self.power += effect.get("power", 0)
        return self.power

    def add_hp(self) -> int:
        if self.potion and isinstance(self.potion, dict):
            effect = self.potion.get("effect")
            if isinstance(effect, dict):
                self.hp += effect.get("hp", 0)
        return self.hp
