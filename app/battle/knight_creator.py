class Knight:

    def __init__(
            self,
            knight_params: dict,
            list_order: int
    ) -> None:
        self.name = knight_params["name"]
        self.power = knight_params["power"]
        self.hp = knight_params["hp"]
        self.armour = self.full_armour(knight_params["armour"])
        self.weapon = knight_params["weapon"]
        self.potion = knight_params["potion"]
        self.list_order = list_order

    def __repr__(self) -> str:
        return f"{self.name} - Health: {self.hp}"

    def __str__(self) -> str:
        return f"{self.name} - Health: {self.hp}"

    def __getitem__(self, key: str) -> str:
        return getattr(self, key)

    @staticmethod
    def full_armour(armour: list) -> int:
        return sum(part["protection"] for part in armour)

    def use_potion(self) -> None:
        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                if key == "power":
                    self.power += value
                if key == "hp":
                    self.hp += value
                if key == "protection":
                    self.armour += value

    def attack(self) -> int:
        return self.power + self.weapon["power"]

    def defence(self, damage: int) -> None:
        self.hp -= damage - self.armour
        if self.hp <= 0:
            self.hp = 0
