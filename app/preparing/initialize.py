from app.preparing.knight import Knight


team_composition = {}


def initialize(knights: dict) -> dict:
    for knight in knights.values():

        if knight["armour"]:
            knight["protection"] = sum(
                arm["protection"] for arm in knight["armour"]
            )
        else:
            knight["protection"] = 0

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            for effect, value in (knight["potion"]["effect"]).items():
                knight[effect] += value

        new_member = Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            knight["protection"]
        )

        team_composition[new_member.name] = new_member
    return team_composition
