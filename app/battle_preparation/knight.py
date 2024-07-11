class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.equipment = None
        self.liquid = None
        self.weapon = None

    def get_ready_for_battle(self,
                             armor_parts: list,
                             miracle_potion: dict,
                             divine_weapon: dict) -> None:
        from app.battle_preparation.armour import Armour
        armour = Armour.prepare_armour(armor_parts)
        armour.consider_armour_effect(self)
        from app.battle_preparation.potion import Potion
        potion = Potion.drink_potion(miracle_potion)
        if potion:
            potion.consider_potion_effect(self)
        from app.battle_preparation.weapon import Weapon
        weapon = Weapon.prepare_weapon(divine_weapon)
        weapon.consider_weapon(self)
