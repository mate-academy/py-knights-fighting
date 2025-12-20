class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: list[dict[str, int]],
            weapon: dict[str, int],
            potion: dict[str, dict[str, int]] | None = None
    ) -> None:

        self.name = name
        self.base_hp = hp
        self.base_power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.current_hp = hp
        self.current_power = power
        self.current_protection = 0

    def apply_equipment(self) -> None:
        self.current_protection = sum(
            part["protection"] for part in self.armour
        )
        self.current_power = self.base_power + self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            self.current_hp += effect.get("hp", 0)
            self.current_power += effect.get("power", 0)
            self.current_protection += effect.get("protection", 0)

    def take_damage(self, amount: int) -> None:
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0

    def prepare_for_battle(self) -> None:
        self.apply_equipment()
        self.apply_potion()

    def is_alive(self) -> bool:
        return self.current_hp > 0
