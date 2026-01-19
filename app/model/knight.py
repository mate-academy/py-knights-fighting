class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

    def apply_armor(self, armour: list) -> None:
        if armour:
            for arm in armour:
                self.protection += arm["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion is not None:
            effect = potion.get("effect", {})
            self.protection += effect.get('protection', 0)
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)

    @classmethod
    def prepare_knight(cls, data: dict) -> "Knight":
        base_knight = cls(
            data["name"],
            data["hp"],
            data["power"]
        )
        base_knight.apply_armor(data["armour"])
        base_knight.apply_weapon(data["weapon"])
        base_knight.apply_potion(data["potion"])
        return base_knight
