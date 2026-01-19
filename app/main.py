from app.model.knight import Knight
from app.model.battle import battle_between_knights


def battle(knightsConfig: dict) -> dict:
    lancelot = knightsConfig["lancelot"]
    lancelot_knight = Knight.prepare_knight(lancelot)
    arthur = knightsConfig["arthur"]
    arthur_knight = Knight.prepare_knight(arthur)
    mordred = knightsConfig["mordred"]
    mordred_knight = Knight.prepare_knight(mordred)
    red_knight = knightsConfig["red_knight"]
    knight_red_knight = Knight.prepare_knight(red_knight)
    battle_between_knights(lancelot_knight, mordred_knight)
    battle_between_knights(arthur_knight, knight_red_knight)
    return {
        lancelot_knight.name: lancelot_knight.hp,
        mordred_knight.name: mordred_knight.hp,
        arthur_knight.name: arthur_knight.hp,
        knight_red_knight.name: knight_red_knight.hp,
    }
