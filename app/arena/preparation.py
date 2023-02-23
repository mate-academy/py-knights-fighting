from app.hall.fighters import Fighters


class Prepare:
    @staticmethod
    def fighter_preparation(fighter: Fighters) -> None:
        Prepare.armour_prepare(fighter)
        Prepare.weapon_prepare(fighter)
        Prepare.potion_prepare(fighter)

    @staticmethod
    def armour_prepare(fighter: Fighters) -> None:
        for armour in fighter.armour:
            fighter.protection += armour["protection"]

    @staticmethod
    def weapon_prepare(fighter: Fighters) -> None:
        fighter.power += fighter.weapon["power"]

    @staticmethod
    def potion_prepare(fighter: Fighters) -> None:
        if fighter.potion is not None:
            for key, value in fighter.potion["effect"].items():
                old_value = getattr(fighter, key)
                setattr(fighter, key, old_value + value)
