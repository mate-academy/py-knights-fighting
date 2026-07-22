class Knight:

    def __init__(self, knight_dict: dict) -> None:
        self.name = knight_dict["name"]
        self.base_power = knight_dict["power"]
        self.base_hp = knight_dict["hp"]
        self.armour = knight_dict.get("armour", [])
        self.weapon = knight_dict["weapon"]
        self.potion = knight_dict.get("potion")

    @classmethod
    def from_dict(cls, knight_dict: dict) -> "Knight":
        return cls(knight_dict)

    def __repr__(self) -> str:
        return str(self.to_dict())

    @property
    def power(self) -> int:
        power = self.base_power
        power += self.weapon.get("power", 0)
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                power += self.potion["effect"]["power"]

        return power

    @property
    def hp(self) -> int:
        hp = self.base_hp
        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                hp += self.potion["effect"]["hp"]

        return hp

    @property
    def protection(self) -> int:
        protection = 0
        for item in self.armour:
            protection += item["protection"]
        if self.potion is not None:
            if "protection" in self.potion["effect"]:
                protection += self.potion["effect"]["protection"]

        return protection

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "power": self.base_power,
            "hp": self.base_hp,
            "armour": self.armour,
            "weapon": self.weapon,
            "potion": self.potion
        }
