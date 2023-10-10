from ..ammunition.armour import Armour
from ..ammunition.weapons import Weapon
from ..ammunition.potions import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = None
        self.potion = None

    def put_on_armour(self, armour: list[dict]) -> None:
        if not armour:
            return
        armour = Armour.parse_armour(armour)
        self.armour.extend(armour)
        self.protection += sum([part.protection for part in armour])

    def apply_weapon(self, weapon: dict | None) -> None:
        if not weapon:
            return
        self.weapon = Weapon(**weapon)
        self.power += self.weapon.power

    def apply_potion(self, potion: dict | None) -> None:
        if not potion:
            return
        self.potion = Potion(**potion)
        self.power += self.potion.effect.get("power", 0)
        self.hp += self.potion.effect.get("hp", 0)
        self.protection += self.potion.effect.get("protection", 0)

    @classmethod
    def prepare_to_battle(cls, knight: dict) -> "Knight":
        knight_instance = Knight(knight["name"], knight["power"], knight["hp"])
        knight_instance.put_on_armour(knight["armour"])
        knight_instance.apply_weapon(knight["weapon"])
        knight_instance.apply_potion(knight["potion"])
        return knight_instance

    @staticmethod
    def knights_battle(knight1: "Knight", knigh2: "Knight") -> None:
        knight1.hp = max(0, knight1.hp - (knigh2.power - knight1.protection))
        knigh2.hp = max(0, knigh2.hp - (knight1.power - knigh2.protection))
