from app.preparing.knight import Knight


def initialize(knights: dict) -> dict:
    team_composition = {}
    for knight in knights.values():
        protection = sum(arm["protection"] for arm in knight["armour"])
        power = knight["weapon"]["power"] + knight["power"]
        hp = knight["hp"]
        if knight["potion"] is not None:
            for effect, value in (knight["potion"]["effect"]).items():
                if effect == "protection":
                    protection += value
                elif effect == "power":
                    power += value
                elif effect == "hp":
                    hp += value
        new_member = Knight(
            knight["name"],
            power,
            hp,
            protection
        )
        team_composition[new_member.name] = new_member
    return team_composition
