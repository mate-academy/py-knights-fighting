class Fall:

    @staticmethod
    def change_hp(fighter, power_opponent):
        fighter.hp -= power_opponent - fighter.protection
        if fighter.hp <= 0:
            fighter.hp = 0
