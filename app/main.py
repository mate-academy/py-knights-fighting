from app.Knights import Knights
from app.Battle import Battle


def battle(knights: dict) -> dict:
    competitors = {knight["name"]: Knights(knight["name"],
                                           knight["power"],
                                           knight["hp"],
                                           knight["armour"],
                                           knight["weapon"],
                                           knight["potion"])
                   for knight in knights.values()
                   }

    for knight in competitors.values():
        knight.add_equipment()

    Battle.competition(competitors["Lancelot"], competitors["Mordred"])
    Battle.competition(competitors["Artur"], competitors["Red Knight"])

    return {
        competitors["Lancelot"].name: competitors["Lancelot"].hp,
        competitors["Artur"].name: competitors["Artur"].hp,
        competitors["Mordred"].name: competitors["Mordred"].hp,
        competitors["Red Knight"].name: competitors["Red Knight"].hp
    }
