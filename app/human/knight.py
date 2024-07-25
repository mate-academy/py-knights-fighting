"""
In this module we store the Knight class
and what it has.
Thus implementing the relationship "HAS-A"

actually he(each knight) doesn't have all of this all the time,
only during battle,
but it all belongs to him
"""


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = None
        self.weapon = None
        self.squire = None
        self.potion = None

    def apply_armour(self) -> None:
        additional_power: int = sum(
            armor["power"] for armor in self.squire.armor_list
        )
        self.armor = self.Armor(
            part="self.armor.name",
            power=self.armor.power + additional_power
        )

    def apply_weapon(self) -> None:
        self.weapon = Knight.Weapon(
            name=self.squire.weapon.name,
            power=self.squire.weapon.power
        )
        self.power += self.squire.weapon.power

    def apply_potion(self):
        if self.squire.potion:
            self.potion = Knight.Potion(
                name=self.squire.potion["name"],
                effects=self.squire.potion["effects"]
            )
            for effect, value in self.potion.effects.items():
                if effect == "power":
                    self.power += value
                elif effect == "hp":
                    self.hp += value
                elif effect == "protection":
                    self.armor.power += value

    class Armor:
        def __init__(self, part: str, power: int) -> None:
            self.part = part
            self.power = power

    class Weapon:
        def __init__(self, name: str, power: int) -> None:
            self.name = name
            self.power = power

    class Potion:
        def __init__(self, name: str, effects: dict[str: int]) -> None:
            self.name = name
            self.effects = effects
