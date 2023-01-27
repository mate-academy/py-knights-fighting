from app.knights.knight import Knight


# зініціюємо функцію для створення екземплярів класу Knight - лицарів:

def create_knight(knight: str, knights: dict) -> Knight:
    return (
        Knight(
            name=knights[knight]["name"],
            power=knights[knight]["power"],
            hp=knights[knight]["hp"],
            armour=knights[knight]["armour"],
            weapon=knights[knight]["weapon"],
            potion=knights[knight]["potion"]
        )
    )
