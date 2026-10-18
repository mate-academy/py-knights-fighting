class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        self._apply_armour(config["armour"])
        self._apply_weapon(config["weapon"])
        self._apply_potion(config["potion"])

    def _apply_armour(self, armour: list) -> None:
        self.protection = sum(
            part["protection"]
            for part in armour
        )

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return

        for stat, value in potion["effect"].items():
            setattr(
                self,
                stat,
                getattr(self, stat) + value,
            )
