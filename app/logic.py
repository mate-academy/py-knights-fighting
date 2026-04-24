from app.models import Knight


def prepare_knight(config: dict) -> Knight:
    knight = Knight(**config)

    knight.protection = sum(a["protection"] for a in knight.armour)
    knight.power += knight.weapon["power"]

    if knight.potion:
        for stat, value in knight.potion["effect"].items():
            if stat == "power":
                knight.power += value
            elif stat == "protection":
                knight.protection += value
            elif stat == "hp":
                knight.hp += value

    return knight


def battle(knights_config: dict) -> dict:
    lancelot, arthur, mordred, red_knight = [
        prepare_knight(v) for v in knights_config.values()
    ]

    lancelot.hp -= max(mordred.power - lancelot.protection, 0)
    mordred.hp -= max(lancelot.power - mordred.protection, 0)

    arthur.hp -= max(red_knight.power - arthur.protection, 0)
    red_knight.hp -= max(arthur.power - red_knight.protection, 0)

    return {
        k.name: max(k.hp, 0)
        for k in [lancelot, arthur, mordred, red_knight]
    }
