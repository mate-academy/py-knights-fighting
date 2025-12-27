from app.game_objects.game_object import GameObject


class Weapon(GameObject):
    def __init__(
            self,
            name: str,
            power: int = 0,
    ) -> None:
        super().__init__(name)
        self.power = power
