from app.Knights import Knights
from app.Battle import Battle


def battle(knights: dict) -> dict:
    competitors = [
        Knights(knight["name"],
                knight["power"],
                knight["hp"],
                knight["armour"],
                knight["weapon"],
                knight["potion"])
        for knight in knights.values()
    ]
    for knight in competitors:
        knight.add_equipment()
    Battle.competition(competitors[0], competitors[2])
    Battle.competition(competitors[1], competitors[3])

    return {
        competitors[0].name: competitors[0].hp,
        competitors[1].name: competitors[1].hp,
        competitors[2].name: competitors[2].hp,
        competitors[3].name: competitors[3].hp
    }
