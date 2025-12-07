from app.models import Knight


def battle(knightsconfig: dict) -> dict:
    # tworzymy rycerzy na podstawie konfiguracji
    lancelot = Knight(knightsconfig["lancelot"])
    arthur = Knight(knightsconfig["arthur"])
    mordred = Knight(knightsconfig["mordred"])
    red_knight = Knight(knightsconfig["red_knight"])

    # przygotowanie (zbroja, broń, mikstury)
    for knight in (lancelot, arthur, mordred, red_knight):
        knight.prepare()

    # --- 1. Lancelot vs Mordred ---
    dmg_to_lancelot = max(0, mordred.power - lancelot.protection)
    dmg_to_mordred = max(0, lancelot.power - mordred.protection)

    lancelot.hp = max(0, lancelot.hp - dmg_to_lancelot)
    mordred.hp = max(0, mordred.hp - dmg_to_mordred)

    # --- 2. Arthur vs Red Knight ---
    dmg_to_arthur = max(0, red_knight.power - arthur.protection)
    dmg_to_red_knight = max(0, arthur.power - red_knight.protection)

    arthur.hp = max(0, arthur.hp - dmg_to_arthur)
    red_knight.hp = max(0, red_knight.hp - dmg_to_red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
