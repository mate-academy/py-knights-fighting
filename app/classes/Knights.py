class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict | None = None,
        potion: dict | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __repr__(self) -> str:
        str_return = f"Knight(name={self.name}, power={self.power}, "
        str_return += f"hp={self.hp}, armour={self.armour}, "
        str_return += f"weapon={self.weapon}, potion={self.potion})"
        return str_return

    def __str__(self) -> str:
        return f"{self.name} (Power: {self.power}, HP: {self.hp})"

    def inicializate_stats(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)
        self.power += self.weapon["power"]
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
