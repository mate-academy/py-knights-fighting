from app.game_objects.game_object import GameObject


class Armour(GameObject):
    def __init__(
            self,
            name: str,
            protection: int = 0
    ) -> None:
        super().__init__(name)
        self.protection = protection
