from __future__ import annotations

from app.knights.knight import Knight


class PreparedKnight:
    def __init__(self, knight: Knight) -> None:
        self.name = knight.name
        self.power = knight.power + knight.potion.power + knight.weapon.power
        self.protection = knight.potion.protection + sum(
            [armour.protection for armour in knight.armour]
        )
        self.hp = knight.hp + knight.potion.hp
