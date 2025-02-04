from app.items.apparel import Apparel
from app.items.weapon import Weapon
from app.items.potion import Potion
from app.items.potion_effect import PotionEffect


class GearSet:
    @staticmethod
    def prepare_gear_for_knights() -> dict:
        lancelot_gear = GearSet(Weapon("Metal Sword", 50))
        arthur_gear = GearSet(Weapon("Two-Handed Sword", 55),
                              [Apparel("helmet", 15),
                               Apparel("breastplate", 20),
                               Apparel("boots", 10)])
        mordred_gear = GearSet(Weapon("Poisoned Sword", 60),
                               [Apparel("breastplate", 15),
                               Apparel("boots", 10)],
                               [Potion("Berserk", [PotionEffect("power", 15),
                                                  PotionEffect("hp", -5),
                                                  PotionEffect("protection",
                                                               10)])])
        red_knight_gear = GearSet(Weapon("Sword", 45),
                                  [Apparel("breastplate", 25)],
                                  [Potion("Blessing", [PotionEffect("hp", 10),
                                                      PotionEffect("power", 5)])])
        return {"Lancelot": lancelot_gear,
                "Arthur": arthur_gear,
                "Mordred": mordred_gear,
                "Red Knight": red_knight_gear}

    def __init__(
            self, weapon: Weapon,
            apparel: list[Apparel],
            potions: list[Potion]) -> None:
        self.weapon = weapon
        self.apparel = apparel
        self.potions = potions
