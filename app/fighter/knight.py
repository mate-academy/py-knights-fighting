from app.gear.armour import Armour
from app.gear.potion import Potion
from app.gear.weapon import Weapon


class Knight:
    """Represents a knight in combat, managing stats,
     equipment, and interactions.

        Attributes:
            name (str): The name of the knight.

            hp (int): The current hit points of the knight.

            base_power (int): The base power of the knight
            without equipment bonuses.

            protection (int): The total protection
            value provided by equipped armour.

            power (int): The total attack power of the knight
            including equipment bonuses.

            armour_pieces (list[Armour]): A list of armour
            pieces equipped by the knight.

            weapon (Weapon | None): The weapon
            equipped by the knight, if any.

            potion (Potion | None): The potion used or
            available to the knight, if any.
        """

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list | None = None,
                 weapon: dict | None = None,
                 potion: dict | None = None) -> None:
        """INIT"""
        self.name = name
        self.hp = hp
        self.protection = 0
        self.power = power

        self.armour_pieces = [Armour(**a) for a in armour] if armour else []
        self.weapon = Weapon(**weapon) if weapon is not None else None
        self.potion = Potion(**potion) if potion is not None else None

    def wear_armour(self) -> None:
        """Calculates and sets the total protection rating
        based on all equipped armour pieces."""
        self.protection = sum(piece.protection for piece in self.armour_pieces)

    def draw_weapon(self) -> None:
        """Increases the knight's total power by
        adding the weapon's power value."""
        self.power += self.weapon.power

    def use_potion(self) -> None:
        """Applies the effects of the equipped potion
        to the knight's relevant stats safely."""
        if not self.potion:
            return

        allowed_stats = {"hp", "power", "protection"}
        for stat, value in self.potion.effect.items():
            if stat in allowed_stats and hasattr(self, stat):
                current = getattr(self, stat)
                setattr(self, stat, current + value)

    def hit_exchange(self, opponent: Knight) -> None:
        """Executes a mutual attack exchange between
        this knight and an opponent.

            Args:
                opponent (Knight): The opposing knight
                engaged in the hit exchange.
        """
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        self.exceed_threshold()
        opponent.exceed_threshold()

    def exceed_threshold(self) -> None:
        """Ensures the knight's hit points do not drop below zero."""
        if self.hp <= 0:
            self.hp = 0
