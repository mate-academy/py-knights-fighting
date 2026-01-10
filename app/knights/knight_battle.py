from app.knights.knights_init import Knight
from app.knights.result_fight import fight


def battle(knightsconfig: dict) -> dict:
    lancelot = Knight(knightsconfig["lancelot"])
    lancelot_update = lancelot.preparation_knight()

    arthur = Knight(knightsconfig["arthur"])
    arthur_update = arthur.preparation_knight()

    mordred = Knight(knightsconfig["mordred"])
    mordred_update = mordred.preparation_knight()

    red_knight = Knight(knightsconfig["red_knight"])
    red_knight_update = red_knight.preparation_knight()

    lancelot_hp, mordred_hp = fight(lancelot_update, mordred_update)
    arthur_hp, red_knight_hp = fight(arthur_update, red_knight_update)

    return {
        lancelot_hp.name: lancelot_hp.hp,
        arthur_hp.name: arthur_hp.hp,
        mordred_hp.name: mordred_hp.hp,
        red_knight_hp.name: red_knight_hp.hp,
    }
