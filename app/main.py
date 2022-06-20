from app.knights import reg_knight
from app.preparation import prepare_for_fight
from app.fight import fight


def battle(knights):

    fighters = reg_knight(knights)

    prepared_fighters = prepare_for_fight(fighters)

    after_battle_fighter = fight(prepared_fighters)

    return {fighter.name: fighter.hp
            for fighter in after_battle_fighter.values()}
