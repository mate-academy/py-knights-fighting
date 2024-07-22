from app.knight import Knight


class Battle:
    def __init__(self, knights_config: dict) -> None:
        self.knights = {
            name: self.create_knight(config)
            for name, config in knights_config.items()
        }

    @staticmethod
    def create_knight(config: dict) -> "Knight":
        return Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )

    def fight(self) -> None:
        self.knights["lancelot"].take_damage(self.knights["mordred"].power)
        self.knights["mordred"].take_damage(self.knights["lancelot"].power)

        self.knights["arthur"].take_damage(self.knights["red_knight"].power)
        self.knights["red_knight"].take_damage(self.knights["arthur"].power)

    def get_results(self) -> dict:
        return {
            knight.name: knight.hp
            for knight in self.knights.values()
        }
