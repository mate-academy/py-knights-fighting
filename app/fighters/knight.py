from app.fighters.tools.poiton import Potion
from app.fighters.tools.weapon import Weapon
from app.fighters.tools.armour import Armour


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list[Armour], weapon: Weapon,
                 potion: Potion | None, protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    @classmethod
    def create_knight_objects(cls, knight_config: dict) -> list["Knight"]:
        knight_result_list = []

        # creating a new instance of knight using dict
        for knight in knight_config:
            name = knight_config[knight]["name"]
            power = knight_config[knight]["power"]
            hp = knight_config[knight]["hp"]
            armour = Armour.get_instances(knight_config[knight]["armour"])
            weapon = Weapon.get_instance(knight_config[knight]["weapon"])
            potion = Potion.get_instance(knight_config[knight]["potion"])

            knight_result_list.append(
                cls(name=name, power=power, hp=hp,
                    armour=armour, weapon=weapon, potion=potion)
            )

        return knight_result_list

    def preparing_for_battle(self) -> "Knight":
        self.power += self.weapon.power
        self.protection = sum(arm.protection for arm in self.armour)

        # looking for different effects
        if self.potion:
            self.power += self.potion.if_effect_exist_return_value("power")
            self.hp += self.potion.if_effect_exist_return_value("hp")
            self.protection += (self.potion
                                .if_effect_exist_return_value("protection"))

        return self

    def battle_with(self, other: "Knight") -> None:
        self.hp -= other.power - self.protection

    def check_if_defeated(self) -> None:
        if self.is_defeated():
            self.hp = 0

    def is_defeated(self) -> bool:
        return self.hp <= 0
