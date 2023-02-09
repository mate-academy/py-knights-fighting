from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour] = None,
                 weapon: Weapon = None,
                 potion: Potion = None) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour if armour else []
        self.weapon = weapon
        self.potion = potion

    def potion_bonus(self, potion: Potion) -> None:
        if potion.effect.power:
            self.power += self.potion.effect.power
        if potion.effect.protection:
            self.protection += self.potion.effect.protection
        if potion.effect.hp:
            self.hp += self.potion.effect.hp

    def calculate_protection(self) -> None:
        for armour in self.armour:
            self.protection += armour.protection

    def calculate_power(self) -> None:
        self.power += self.weapon.power

    def hp_checker(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    @staticmethod
    def knights_to_dict(knights_instances: list[Knight]) -> dict:
        return {
            knights_instances[0].name: knights_instances[0].hp,
            knights_instances[1].name: knights_instances[1].hp,
            knights_instances[2].name: knights_instances[2].hp,
            knights_instances[3].name: knights_instances[3].hp,
        }

    @staticmethod
    def make_list_of_knights(knights_config: dict) -> list[Knight]:
        knights_instances = []
        for knight_name in knights_config:
            knight_dict = knights_config[knight_name]

            armours_list = []
            if knight_dict.get("armour"):
                armours_list = Armour.make_armour(knight_dict.get("armour"))

            weapon = Weapon(name=knight_dict["weapon"]["name"],
                            power=knight_dict["weapon"]["power"])

            potion = None
            if knight_dict.get("potion"):
                potion = Potion.make_potion(knight_dict.get("potion"))

            new_knight = Knight(name=knight_dict["name"],
                                power=knight_dict["power"],
                                hp=knight_dict["hp"],
                                armour=armours_list,
                                weapon=weapon,
                                potion=potion)
            new_knight.protection = 0

            if potion:
                new_knight.potion_bonus(potion)

            new_knight.calculate_protection()
            new_knight.calculate_power()
            knights_instances.append(new_knight)

        return knights_instances


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def make_armour(armour_for_knight: list[dict]) -> list[Armour]:
        armours_list = []
        for armour in armour_for_knight:
            new_armour = Armour(part=armour["part"],
                                protection=armour["protection"])
            armours_list.append(new_armour)
        return armours_list


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Effect:
    def __init__(self, hp: int, power: int, protection: int = None) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect

    @staticmethod
    def make_potion(potion_dict: dict) -> Potion:
        effect = Effect(hp=potion_dict["effect"]["hp"],
                        power=potion_dict["effect"]["power"],
                        protection=potion_dict["effect"].get("protection"))

        potion = Potion(name=potion_dict["name"],
                        effect=effect)

        return potion
