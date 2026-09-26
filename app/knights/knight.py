class Knight:

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: dict | None = None,
    ) -> None:
        self.name: str = name
        self.hp: int = hp

        self.power: int = power + weapon["power"]

        self.protection: int = sum(item["protection"] for item in armour)

        if potion is not None:
            effects = potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
