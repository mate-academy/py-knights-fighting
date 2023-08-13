from app.config.armour import Armour
from app.config.weapon import Weapon
from app.config.potion import Potion


class BattleKit:
    def __init__(
            self,
            armour: list[dict] = None,
            weapon: dict = None,
            potion: dict = None
    ) -> None:
        """
        Constructor for the BattleKit class

        This constructor initializes a BattleKit object
        with optional armour, weapon, and potion
        It creates Armour and Weapon instances using
        the provided data and assigns them to the object's attributes
        """
        self.armour = [Armour(part) for part in armour]
        self.weapon = Weapon(weapon)
        self.potion = Potion(potion)
