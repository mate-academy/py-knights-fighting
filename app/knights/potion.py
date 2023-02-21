from app.knights.knight import Knight


class Potion:

    def __init__(self, name: str, effect: int) -> None:
        self.name = name
        self.effect = effect

    def apply_potion(self, knight: Knight) -> None:
        if self:
            knight.power += self.effect
            knight.hp += self.effect
            for armour in knight.armours:
                armour.update_protection(knight, self.effect)

        elif self.effect < 0:
            knight.power -= self.effect
            knight.hp -= self.effect
            for armour in knight.armours:
                armour.update_protection(knight, self.effect)



