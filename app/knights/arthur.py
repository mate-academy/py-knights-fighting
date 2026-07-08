# Knight ARTHUR
from app.knights.knight import Knight


class Arthur(Knight):
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict = None
    ) -> None:
        super().__init__(
            name, power, hp, armour, weapon, potion
        )
