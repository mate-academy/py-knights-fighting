from __future__ import annotations
from app.item import Item


class Knight:
    """
    Represents a knight in object with attributes of name, health points(hp),
    armor points(ap), power and 2 types of invetory
    All armour is applied to each knight before entering the battle
    has methods
    """
    def __init__(
        self,
        name: str,
        initial_power: int,
        initial_hp: int,
    ) -> None:
        """initializes our knight instance with basic stats"""
        self.name = name
        self.power = initial_power
        self.hp = initial_hp
        self.ap = 0                # armor is initially 0 - need to equip first
        self.equipment = list()    # fills up (or not) after take_items call
        self.inventory = list()    # also depends on result of take_items call

    def __repr__(self) -> str:
        return f"This is {self.name} " \
               f"with {self.hp} hp, {self.power} power, {self.ap} protection."

    def take_items(self, items: list(Item)) -> None:
        """
        Takes a list of items and sorts them
        between lists of usables and equippables
        after sortin it calls use_items method with equippables
        so the knight could be well armored well before battle
        """
        for item in items:
            if item.item_kind == "equip":
                self.equipment.append(item)
            elif item.item_kind == "use":
                self.inventory.append(item)
        self.use_items(self.equipment)

    def use_items(self, items: list = None) -> None:
        """
        goes through list of items and applies stat modiefiers
        when called without an argument goes through the usable items
        may be expanded if more stats implemented in Knight class
        """
        if not items:
            items = self.inventory
        for item in items:
            if "protection" in item.stats:
                self.ap += item.stats["protection"]
            if "power" in item.stats:
                self.power += item.stats["power"]
            if "hp" in item.stats:
                self.hp += item.stats["hp"]

    def get_strike(self, strike_power: int) -> None:
        """
        calculates damage recieved from opponents attack, changes attribute hp
        """
        self.hp -= strike_power - self.ap
        self.hp = max(self.hp, 0)
