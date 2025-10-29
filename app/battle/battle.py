class Battle:
    def __init__(self, knights: dict) -> None:
        self.knights = knights

    def start_battle(self) -> dict:
        pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
        for first_group, second_group in pairs:
            first_group_knight = self.knights[first_group]
            second_group_knight = self.knights[second_group]
            self.duel(first_group_knight, second_group_knight)

        result_battle = {}
        for name in self.knights.keys():
            result_battle.update({self.knights[name]["name"]: self.knights[name]["hp"]})
        return result_battle

    def duel(self, first_group: dict, second_group: dict) -> None:
        damage_to_second = max(0, first_group["power"] - second_group["protection"])
        damage_to_first = max(0, second_group["power"] - first_group["protection"])
        first_group["hp"] = max(0, first_group["hp"] - damage_to_first)
        second_group["hp"] = max(0, second_group["hp"] - damage_to_second)

