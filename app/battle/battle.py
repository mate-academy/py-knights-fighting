from app.battle.knight import Knight
from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


class Battle:
    # Create instances of items
    @staticmethod
    def initialize_items(knights: dict[dict]) -> None:
        for knight, config in knights.items():
            # Create instance of Weapon (in place of dict)
            config["weapon"] = Weapon(
                config["weapon"]["name"],
                config["weapon"]["power"]
            )
            # Create instance of Potion (in place of dict)
            if config.get("potion"):
                config["potion"] = Potion(
                    config["potion"]["name"],
                    config["potion"]["effect"]
                )

    # Create instances of knights
    @staticmethod
    def initialize_knights(knights: dict[dict]) -> None:
        Battle.print_separator()

        for knight, config in knights.items():
            # Create a list of armour parts
            armour_list = []
            for piece_of_armour in config["armour"]:
                armour_list.append(
                    Armour(
                        piece_of_armour.get("part"),
                        piece_of_armour.get("protection")
                    )
                )
            # Create instance of Knight
            new_knight = Knight(
                config["name"],
                config["power"],
                config["hp"],
                armour_list,
                config["weapon"],
                config["potion"],
            )
            print(f"The knight {new_knight.name} enters the championship!")

        Battle.print_separator()

    # Change Knight attributes
    @staticmethod
    def apply_item_effects(knights: dict) -> None:
        for name, knight in knights.items():

            # Apply armour protection
            # Armour list for message printing
            armour_set = []
            for piece_of_armour in knight.armour:
                knight.protection += piece_of_armour.protection
                armour_set.append(piece_of_armour.name)

            print(
                f"{knight.name} is wearing {Battle.format_armour(armour_set)}"
            )

            # Apply weapon power
            knight.power += knight.weapon.power

            # Apply potion effects if potion exists
            if knight.potion:
                knight.drink_potion(knight.potion)

            # Print separator
            print("-" * 46)

    @staticmethod
    def match(knight_1: Knight, knight_2: Knight) -> dict:
        print(f"The match begins: {knight_1.name} vs {knight_2.name}")

        knight_1.attack(knight_2)
        knight_2.attack(knight_1)

        # Determine if a knight fell in battle
        for knight in [knight_1, knight_2]:
            if knight.has_fallen():
                knight.hp = 0
                print(f"{knight.name} has fallen!")

        Battle.print_separator()

        # Return knight name and remaining HP
        return {
            knight_1.name: knight_1.hp,
            knight_2.name: knight_2.hp
        }

    # Message printing
    @staticmethod
    def format_armour(armour_set: list) -> str:
        if not armour_set:
            return "no armor"
        return "a " + ", ".join(piece for piece in armour_set)

    # Message printing
    @staticmethod
    def print_separator() -> None:
        print("#" + "-" * 44 + "#")
