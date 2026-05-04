class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_power = config["power"]
        self.base_hp = config["hp"]
        self.base_armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

        self.hp = self._calculate_hp()
        self.power = self._calculate_power()
        self.protection = self._calculate_armour()

    def _calculate_hp(self) -> int:
        if self._get_potion_effects("hp"):
            return self.base_hp + self._get_potion_effects("hp")
        return self.base_hp

    def _calculate_power(self) -> int:
        if self._get_potion_effects("power"):
            return (
                self.weapon["power"]
                + self._get_potion_effects("power")
                + self.base_power
            )
        return self.weapon["power"] + self.base_power

    def _calculate_armour(self) -> int:
        if self.base_armour:
            if self._get_potion_effects("protection"):
                return sum(
                    a["protection"] for a in self.base_armour
                ) + self._get_potion_effects("protection")
            return sum(a["protection"] for a in self.base_armour)
        return 0

    def _get_potion_effects(self, effect_type: str) -> int:
        if self.potion is None:
            return 0
        return self.potion["effect"].get(effect_type, 0)

    def __str__(self) -> str:
        return f"HP: {self.hp}, Power: {self.power}, Armour: {self.protection}"

    def get_hp(self) -> int:
        return self.hp

    def get_power(self) -> int:
        return self.power

    def get_protection(self) -> int:
        return self.protection

    def _set_hp(self, hp: int) -> None:
        self.hp = hp

    def take_damage(self, damage: int) -> None:
        if self.hp - damage < 0:
            self._set_hp(0)
        else:
            self._set_hp(self.hp - damage)

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def get_stats(self) -> dict:
        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection,
        }
