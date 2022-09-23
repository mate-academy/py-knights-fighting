from app.knights import Knights


def health_check(knights_hp: int) -> int:
    if knights_hp <= 0:
        return 0

    return knights_hp


def battle(knights_config: dict) -> dict:
    lancelot = Knights(knights_config["lancelot"])
    arthur = Knights(knights_config["arthur"])
    mordred = Knights(knights_config["mordred"])
    red_knight = Knights(knights_config["red_knight"])

    lancelot.battle_preparation()
    arthur.battle_preparation()
    mordred.battle_preparation()
    red_knight.battle_preparation()

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    lancelot.hp = health_check(lancelot.hp)
    mordred.hp = health_check(mordred.hp)

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    arthur.hp = health_check(arthur.hp)
    red_knight.hp = health_check(red_knight.hp)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
