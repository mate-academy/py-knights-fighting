class Weapon:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]


class Armor:
    def __init__(self, data: list) -> None:
        # Считаем общую защиту всех частей брони
        self.protection = sum(part["protection"] for part in data)


class Potion:
    def __init__(self, data: dict) -> None:
        if not data:
            self.hp_mod = 0
            self.power_mod = 0
            self.protection_mod = 0
        else:
            effect = data.get("effect", {})
            self.hp_mod = effect.get("hp", 0)
            self.power_mod = effect.get("power", 0)
            self.protection_mod = effect.get("protection", 0)
