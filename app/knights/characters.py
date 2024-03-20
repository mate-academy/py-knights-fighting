from app.knights.items import Armour, Potion, Weapon


class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: list = None,
            weapon: dict = None,
            potion: dict = None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour = [
            Armour(part=ar["part"],
                   protection=ar["protection"]) for ar in armour
        ] if armour else []
        self.weapon = Weapon(name=weapon["name"],
                             power=weapon["power"])
        self.potion = Potion(name=potion["name"],
                             effect=potion["effect"]) if potion else None

    def activate_items(self) -> None:
        self.power += self.weapon.power
        self.protection += sum(
            [
                ar.protection for ar in self.armour
            ]if self.armour else [self.protection])

        if self.potion:
            for key, value in self.potion.effect.items():
                setattr(self, key, getattr(self, key, 0) + value)
