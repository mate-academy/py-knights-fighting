class Knight:
    def __init__(
            self,
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
        self.final_hp = self.calculate_final_hp()
        self.final_protection = self.calculate_final_protection()
        self.final_power = self.calculate_final_power()

    def calculate_final_stat(
            self,
            base_stat: int,
            stat_name: str,
            additional: int = 0
    ) -> int:

        final_stat = base_stat

        final_stat += additional

        if self.potion and stat_name in self.potion["effect"]:
            final_stat += self.potion["effect"][stat_name]

        return final_stat

    def calculate_final_hp(self) -> int:
        return self.calculate_final_stat(
            self.hp,
            "hp"
        )

    def calculate_final_protection(self) -> int:
        protection_from_armour = sum(
            item["protection"] for item in self.armour
        )
        return self.calculate_final_stat(
            0,
            "protection",
            protection_from_armour
        )

    def calculate_final_power(self) -> int:
        return self.calculate_final_stat(
            self.power,
            "power",
            self.weapon["power"]
        )
