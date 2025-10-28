class Battle:
    def __init__(self, knights: dict) -> None:
        self.knights = knights

    def start_battle(self) -> dict:
        pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
        for first_group, second_group in pairs:
            first_group_knight = self.knights[first_group]
            second_group_knight = self.knights[second_group]
            damage_to_second = max(0 , first_group_knight["power"] - second_group_knight["protection"])
            damage_to_first = max(0 , second_group_knight["power"] - first_group_knight["protection"])
            first_group_knight["hp"] = max(0, first_group_knight["hp"] - damage_to_first)
            second_group_knight["hp"] = max(0, second_group_knight["hp"] - damage_to_second)

        return {
            self.knights["lancelot"]["name"]: self.knights["lancelot"]["hp"],
            self.knights["arthur"]["name"]: self.knights["arthur"]["hp"],
            self.knights["mordred"]["name"]: self.knights["mordred"]["hp"],
            self.knights["red_knight"]["name"]: self.knights["red_knight"]["hp"],
        }
