class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict,
                 potion: dict = None) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = [Armour(a["part"],
                              a["protection"]) for a in armour]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(potion["name"],
                             potion["effect"]) if potion else None

        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        self.power = self.base_power + self.weapon.power
        self.hp = self.base_hp

        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        actual_damage = max(damage - self.protection, 0)
        self.hp = max(self.hp - actual_damage, 0)


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
