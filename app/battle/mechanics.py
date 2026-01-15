from app.models.knight import Knight


def prepare_knights(knights_dict: dict) -> dict:
    return {
        name: Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data.get("potion")
        ).prepare_for_battle()
        for name, data in knights_dict.items()
    }


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.receive_damage(knight2.power - knight1.protection)
    knight2.receive_damage(knight1.power - knight2.protection)
