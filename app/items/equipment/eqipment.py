from app.items.item import BaseItem


class BaseEquipment(BaseItem):
    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0,
            is_equipped: bool = False
    ) -> None:
        super().__init__(name, power, hp, protection)
        self.is_equipped = is_equipped
