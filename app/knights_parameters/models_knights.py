class KnightsParameters:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armor: list,
            weapon: dict,
            potion: dict or None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion

        self.battle_armor = 0
        self.battle_hp = 0
        self.battle_power = 0

    def parameters_in_battle(self) -> None:
        effect_power = self.potion["effect"]["power"] \
            if self.potion and "power" in self.potion["effect"] else 0
        effect_hp = self.potion["effect"]["hp"] \
            if self.potion and "hp" in self.potion["effect"] else 0
        effect_protection = self.potion["effect"]["protection"] \
            if self.potion and "protection" in self.potion["effect"] else 0

        for protection in self.armor:
            effect_protection += protection["protection"]

        self.battle_power = self.power + self.weapon["power"] + effect_power
        self.battle_hp = self.hp + effect_hp
        self.battle_armor = effect_protection
