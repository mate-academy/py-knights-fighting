class Knight:
    def __init__(
            self,
            name: str,
            base_hp: int,
            base_power: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_stats(self) -> dict:
        armour = sum(
            arm["protection"] for arm in self.armour or []
        )
        power = self.base_power
        hp = self.base_hp
        protection = armour
        power += self.weapon["power"] if self.weapon else 0

        if self.potion:
            effect = self.potion["effect"]
            hp += effect.get("hp", 0)
            protection += effect.get("protection", 0)
            power += effect.get("power", 0)

        return {
            "hp": hp,
            "power": power,
            "protection": protection
        }
