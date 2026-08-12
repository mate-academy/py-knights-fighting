class Knight:

    collection = {}

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    @staticmethod
    def create_knights_with_armour(knights: dict) -> None:
        for knight in knights.values():
            Knight.collection[knight["name"]] = Knight(
                knight["name"],
                knight["power"],
                knight["hp"],
            )

            total_protection = 0

            for piece in knight["armour"]:
                total_protection += piece["protection"]

            Knight.collection[knight["name"]].protection = total_protection

    @staticmethod
    def add_weapon_power(knights: dict) -> None:
        for knight in knights.values():
            Knight.collection[knight["name"]].power += (
                knight["weapon"]["power"]
            )

    @staticmethod
    def apply_potion(knights: dict) -> None:
        for knight in knights.values():
            current_knight = Knight.collection[knight["name"]]

            if knight["potion"] is not None:
                effect = knight["potion"]["effect"]
                if "hp" in effect:
                    current_knight.hp += effect["hp"]

                if "power" in effect:
                    current_knight.power += effect["power"]

                if "protection" in effect:
                    current_knight.protection += effect["protection"]

    @staticmethod
    def initialize_knights(knights: dict) -> None:
        Knight.create_knights_with_armour(knights)
        Knight.add_weapon_power(knights)
        Knight.apply_potion(knights)
