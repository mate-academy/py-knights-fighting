from app.KNIGHTS_list.knight import Knight


def create_knight(data: dict) -> Knight:
    return Knight(
        name=data["name"],
        base_hp=data["hp"],
        base_power=data["power"],
        armour=data["armour"],
        weapon=data["weapon"],
        potion=data["potion"]
    )


def create_all_knights(knights_data: dict) -> dict:
    return {
        knight_name: create_knight(data)
        for knight_name, data
        in knights_data.items()
    }
