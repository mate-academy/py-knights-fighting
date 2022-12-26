import app.equipment as equip


class Knight:
    def __init__(self, knight_cfg: dict) -> None:
        self.name = knight_cfg["name"]
        self.power = knight_cfg["power"]
        self.hp = knight_cfg["hp"]
        self.armour = equip.Armour(knight_cfg["armour"])
        self.weapon = equip.Weapon(knight_cfg["weapon"])
        self.potion = (
            equip.Potion(knight_cfg["potion"])
            if knight_cfg["potion"]
            else None
        )

    @property
    def hit_power(self) -> int:
        potion_power = self.potion.power if self.potion else 0
        return self.power + self.weapon.power + potion_power

    def take_a_hit(self, hit_power: int) -> None:
        buff = sum(a.protection for a in self.armour)
        if self.potion:
            buff += self.potion.hp + self.potion.protection
        hit_power -= buff
        self.hp -= hit_power
        if self.hp < 0:
            self.hp = 0

    def fight(self, other: "Knight") -> None:
        other.take_a_hit(self.hit_power)
        self.take_a_hit(other.hit_power)
