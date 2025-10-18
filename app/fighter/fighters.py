from app.fighter.fighter import Fighter


class Fighters:
    def __init__(
            self,
            config: dict
    ) -> None:
        self.config = config
        self.fighters = []

    def create_fighters(self) -> None:
        for fighter in self.config.values():
            warrior = Fighter(
                name=fighter["name"],
                power=fighter["power"],
                hp=fighter["hp"],
                armours=fighter["armour"],
                weapon=fighter["weapon"],
                potion=fighter["potion"]
            )
            self.fighters.append(warrior)

    def initiate_fighters(self) -> None:
        for fighter in self.fighters:
            fighter.apply_weapon()
            fighter.apply_armour()
            fighter.apply_potion()

    def get_fighters(self) -> list:
        return self.fighters
