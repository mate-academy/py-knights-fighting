from app.equipment.equipment import Equipment


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.health_points = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        equipment = Equipment(
            armour=self.armour,
            weapon_power=self.weapon["power"]
        )
        equipment.apply_armour(self)
        equipment.apply_weapon(self)
        equipment.apply_potion(self)
