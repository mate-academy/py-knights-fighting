class Knight:
    def __init__(self, data: dict[str, any]) -> None:
        self.name: str = data["name"]
        base_power: int = data["power"]
        base_hp: int = data["hp"]
        armour: list[dict[str, any]] = data.get("armour", [])
        weapon: dict[str, any] = data["weapon"]
        potion: dict[str, any] | None = data.get("potion")

        self.protection: int = sum(a["protection"] for a in armour)

        self.power: int = base_power + weapon["power"]

        self.hp: int = base_hp
        if potion:
            effect: dict[str, int] = potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def __repr__(self) -> str:
        return (
            f"{self.name} (HP: {self.hp}, "
            f"Power: {self.power}, Protection: {self.protection})"
        )
