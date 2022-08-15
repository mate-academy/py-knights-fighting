def battle_round(knight1, knight2):

    def fighting(knight, other_knight):
        knight.hp -= other_knight.power - knight.protection
        other_knight.hp -= knight.power - other_knight.protection

    def checking_if_dead(knight):
        if knight.hp < 0:
            knight.hp = 0

    fighting(knight1, knight2)

    checking_if_dead(knight1)
    checking_if_dead(knight2)
