class Battle:
    @staticmethod
    def get_result(knight_1, knight_2):
        first_knight_hp = knight_1.get_hp()
        second_knight_hp = knight_2.get_hp()
        first_knight_hp -= knight_2.get_power() - knight_1.get_protection()
        second_knight_hp -= knight_1.get_power() - knight_2.get_protection()

        def check_of_death(hp):
            if hp <= 0:
                hp = 0
            return hp

        return {
            knight_1.knight["name"]: check_of_death(first_knight_hp),
            knight_2.knight["name"]: check_of_death(second_knight_hp)
        }
