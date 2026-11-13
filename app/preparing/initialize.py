from app.preparing.knight import Knight


def initialize(knights: dict) -> dict:
    team_composition = {}
    for knight in knights.values():
        knight_copy = knight.copy()
        if knight["armour"]:
            knight_copy["protection"] = sum(
                arm["protection"] for arm in knight["armour"]
            )
        else:
            knight_copy["protection"] = 0
        knight_copy["power"] += knight["weapon"]["power"]
        if knight["potion"] is not None:
            for effect, value in (knight["potion"]["effect"]).items():
                knight_copy[effect] += value
        new_member = Knight(
            knight["name"],
            knight_copy["power"],
            knight_copy["hp"],
            knight_copy["protection"]
        )
        team_composition[new_member.name] = new_member
    return team_composition
