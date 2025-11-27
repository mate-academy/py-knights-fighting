from typing import List, Dict


class KnightConfig:
    """
    Holds and prepares all configuration data for a knight. The raw config
    includes base stats, armour pieces, weapon parameters and potion effects.
    After initialization, armour, weapon and potion are applied to produce
    final combat-ready attributes.

    :param knight_data: dict containing raw knight configuration
    """
    BUFF_TO_ATTR = {
        "hp": "hp",
        "protection": "armour",
        "power": "power",
    }

    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data.get("name")
        self.power = knight_data.get("power")
        self.hp = knight_data.get("hp")

        self.armour = self.calculate_armour(knight_data.get("armour", []))
        self.weapon = knight_data.get("weapon")
        self.potion = knight_data.get("potion")

    @staticmethod
    def calculate_armour(armour_list: List[Dict]) -> int:
        """
        Calculates total armour value for a knight based on all provided
        armour parts. If no armour is present, zero protection is used.

        :param armour_list: list of armour parts with protection values
        :return: int - total protection value
        """
        if not armour_list:
            return 0

        return sum(part.get("protection", 0) for part in armour_list)

    def equip_weapon(self) -> None:
        """
        Applies weapon stats to the knight by adding the weapon's power
        value to the base power attribute.

        :return: None
        """
        self.power += self.weapon.get("power", 0)

    def drink_the_potion(self) -> None:
        """
        Applies potion effects to the knight. Potion may modify hp, power
        or armour based on its defined effect dictionary. Negative and
        positive effects are both supported.

        :return: None
        """
        if not self.potion:
            return

        potion_buffs = self.potion.get("effect", {})

        for key, attr in self.BUFF_TO_ATTR.items():
            setattr(self, attr, getattr(self, attr) + potion_buffs.get(key, 0))

    def prepare(self) -> None:
        """
        Prepares the knight by applying weapon stats and potion effects.
        After preparation, the knight has final hp, power and armour
        values ready for battle.

        :return: None
        """
        for apply_equipment in (self.equip_weapon, self.drink_the_potion):
            apply_equipment()
