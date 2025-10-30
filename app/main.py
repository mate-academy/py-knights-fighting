from app.knights import Knight


def battle(knights_config: list) -> None:
    knights = []
    for identify in knights_config:
        info = knights_config[identify]
        knight_obj = Knight(
            name=info["name"],
            power=info["power"],
            hp=info["hp"],
            weapon=info["weapon"],
            armour=info["armour"],
            potion=info["potion"]
        )
        knights.append(knight_obj)

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]

    battles = [
        (lancelot, mordred),
        (arthur, red_knight)
    ]

    def fight(knight1: object, knight2: object) -> dict:
        knight2.hp -= max(0, knight1.power - knight2.total_protection)
        knight1.hp -= max(0, knight2.power - knight1.total_protection)
        knight1.hp = max(0, knight1.hp)
        knight2.hp = max(0, knight2.hp)

    for k1, k2 in battles:
        fight(k1, k2)

    return {k.name: k.hp for k in knights}
