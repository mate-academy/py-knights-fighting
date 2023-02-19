from app.hall.fighters import Fighters


class Prepare:
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
            if "power" in fighter.potion["effect"]:
                fighter.power += fighter.potion["effect"]["power"]

            if "protection" in fighter.potion["effect"]:
                fighter.protection += fighter.potion["effect"]["protection"]

            if "hp" in fighter.potion["effect"]:
                fighter.hp += fighter.potion["effect"]["hp"]
