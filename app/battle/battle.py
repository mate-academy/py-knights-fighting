class Battle:

    def __init__(self, knights_dict: dict):
        self.knights_dict = knights_dict

    def versus(self, knight_1: str, knight_2: str):
        result_dict = {}
        if self.knights_dict.get(knight_1) and self.knights_dict.get(knight_2):
            self.knights_dict[knight_1].name['hp'] -= \
                self.knights_dict[knight_2].name['power'] \
                - self.knights_dict[knight_1].name['protection']
            self.knights_dict[knight_2].name['hp'] -= \
                self.knights_dict[knight_1].name['power'] \
                - self.knights_dict[knight_2].name['protection']

        check_hp1 = self.check_health_point(
            self.knights_dict[knight_1].name['hp']
        )
        check_hp2 = self.check_health_point(
            self.knights_dict[knight_2].name['hp']
        )

        result_dict.update({knight_1: check_hp1})
        result_dict.update({knight_2: check_hp2})
        return result_dict

    @staticmethod
    def check_health_point(hp):
        if hp <= 0:
            hp = 0
        return hp
