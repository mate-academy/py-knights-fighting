from app.knights.equipment import Weapon, Potion


class Knight:
    def __init__(self, name: str, hp: int, power: int,
                 armour: list | None = None,
                 weapon: Weapon | None = None,
                 potion: Potion | None = None) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

    def prepare_for_battle(self) -> dict:
        hp = self.hp
        power = self.power
        protection = 0

        # броня
        for piece in self.armour:
            protection += piece.protection

        # зброя
        if self.weapon:
            power += self.weapon.power

        # зілля
        if self.potion:
            effect = self.potion.effect
            hp += effect.get("hp", 0)
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)

        return {"hp": hp, "power": power, "protection": protection}
