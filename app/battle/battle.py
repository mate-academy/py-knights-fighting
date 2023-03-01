class Battle:

    @staticmethod
    def knight_equipped(knight):
        knight.power += knight.knights_weapon_equipped()
        if len(knight.armour) >= 1:
            knight.armour = knight.knights_armour_equipping()
        else:
            knight.armour = 0
        if knight.potion is not None:
            (extra_protection,
             extra_power,
             extra_hp) = knight.knights_potion_drinking()
            if extra_power is not None:
                knight.power += extra_power
            if extra_hp is not None:
                knight.hp += extra_hp
            if extra_protection is not None:
                knight.armour += extra_protection

    @staticmethod
    def duel(first_duelist, second_duelist):
        first_duelist.hp -= second_duelist.power - first_duelist.armour
        second_duelist.hp -= first_duelist.power - second_duelist.armour
        if first_duelist.hp <= 0:
            first_duelist.hp = 0
        if second_duelist.hp <= 0:
            second_duelist.hp = 0
