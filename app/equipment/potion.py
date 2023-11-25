from app.contestants.knight import Knight


class Potion:
    def __init__(self, effect: dict | None) -> None:
        self.effect = effect

    # apply potion if exist
    def apply_potion(self, knight: Knight) -> None:
        if knight.potion is not None:
            if "power" in self.effect:
                knight.power += self.effect["power"]

            if "protection" in self.effect:
                knight.protection += self.effect["protection"]

            if "hp" in self.effect:
                knight.health_points += self.effect["hp"]
