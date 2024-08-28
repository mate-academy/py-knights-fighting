from __future__ import annotations


class Hero:
    def __init__(
            self,
            name: str = "Default knight",
            power: int = 20,
            hp: int = 50,
            armor: list = None,
            weapon: dict = None,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor if armor else []
        self.weapon = weapon if weapon else {}
        self.potion = potion if potion else {}
        self.protection = 0

    @classmethod
    def create_from_config(cls, config: dict) -> Hero:
        return cls(
            name=config.get("name"),
            power=config.get("power"),
            hp=config.get("hp"),
            armor=config.get("armour"),
            weapon=config.get("weapon"),
            potion=config.get("potion")
        )

    def put_on_armor(self) -> None:
        if self.armor:
            for item in self.armor:
                self.protection += item["protection"]

    def take_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon["power"]

    def drink_potion(self) -> None:
        if self.potion:
            for name, value in self.potion["effect"].items():
                self.__dict__[name] += value

    def prepare_to_battle(self) -> None:
        self.put_on_armor()
        self.take_weapon()
        self.drink_potion()

    def attack(self, target: Hero) -> None:
        target.hp -= self.power - target.protection
        if target.hp < 0:
            target.hp = 0

    def __repr__(self) -> str:
        hero_info = ""
        hero_info += (
            f"-----------------------------------------------------\n"
            f"Name: {self.name}\n"
            f"Power: {self.power}\n"
            f"HP: {self.hp}\n"
        )

        if self.weapon:
            hero_info += (
                f'Weapon: \n\t{self.weapon.get("name")}, '
                f'power = {self.weapon.get("power")}\n'
            )

        if self.armor:
            details = "".join(
                f'\t{item["part"]} = {item["protection"]}\n'
                for item in self.armor
            )
            hero_info += f"Armor: \n{details}"

        if self.potion:
            details = ", ".join(
                f"{stat} += {value}"
                for stat, value in self.potion.get("effect").items()
            )
            hero_info += f'Potion: \n\t{self.potion.get("name")} {details}\n'

        hero_info += "-----------------------------------------------------\n"
        return hero_info
