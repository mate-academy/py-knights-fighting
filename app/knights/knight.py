class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name: str = knight_data["name"]
        self.power: int = knight_data["power"]
        self.hp: int = knight_data["hp"]
        self.protection: int = 0

        self._apply_armour(knight_data["armour"])
        self._apply_weapon(knight_data["weapon"])
        self._apply_potion(knight_data.get("potion"))

    def _apply_armour(self, armour_pieces: list) -> None:
        for piece in armour_pieces:
            self.protection += piece["protection"]

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: dict | None) -> None:
        if potion:
            effects = potion["effect"]
            self.power += effects.get("power", 0)
            self.hp += effects.get("hp", 0)
            self.protection += effects.get("protection", 0)
