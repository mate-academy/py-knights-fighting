from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict | None = None
                 ) -> None:
        """
        To avoid create new objects every time,
        I back up the initial state to easily heal the knight after the battle.
        """
        self.name, self.name_backup = name, name
        self.power, self.power_name_backup = power, power
        self.hp, self.hp_backup = hp, hp
        self.armour, self.armour_backup = armour, armour
        self.weapon, self.weapon_backup = weapon, weapon
        self.potion, self.potion_backup = potion, potion
        self.protection = 0

    @classmethod
    def init_from_dict(cls, data: dict) -> list[Knight]:
        """
        Create a list of Knight objects from a dictionary.
        """
        knights = []
        for key, knight_data in data.items():
            knights.append(
                cls(
                    name=knight_data["name"],
                    power=knight_data["power"],
                    hp=knight_data["hp"],
                    armour=knight_data["armour"],
                    weapon=knight_data["weapon"],
                    potion=knight_data.get("potion"),
                )
            )
        return knights

    def battle_preparations(self) -> None:
        """
        Prepare the knight for battle by applying:
        armour, weapon, and potion effects.
        """
        self.protection = sum(piece["protection"] for piece in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            self.hp += self.potion["effect"].get("hp", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)

    def heal(self) -> None:
        """
        Healing a knight, returning the parameters that were at initialization
        """
        self.name = self.name_backup
        self.power = self.power_name_backup
        self.hp = self.hp_backup
        self.armour = self.armour_backup
        self.weapon = self.weapon_backup
        self.potion = self.potion_backup
        self.protection = 0

    def get_hp(self) -> dict:
        return {self.name: self.hp}

    def make_damage(self, other: Knight) -> None:
        other.hp -= self.power - other.protection
        if other.hp <= 0:
            other.hp = 0
