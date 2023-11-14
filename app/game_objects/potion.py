from app.game_objects.game_object import GameObject


class Potion(GameObject):
    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        super().__init__(name)
        self.power = power
        self.hp = hp
        self.protection = protection
