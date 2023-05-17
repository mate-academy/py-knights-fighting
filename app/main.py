from app.knights_config import KNIGHTS


class Battle:
    def __init__(self, knights_config: dict) -> None:
        self.knights = knights_config

    def calculate_knight_protection(self, knight: str) -> None:
        knight = self.knights[knight]
        knight["protection"] = 0
        for item in knight["armour"]:
            knight["protection"] += item["protection"]

    def calculate_knight_power(self, knight: str) -> None:
        knight = self.knights[knight]
        knight["power"] += knight["weapon"]["power"]

    def use_potion(self, knight: str) -> None:
        knight = self.knights[knight]
        if knight["potion"]:
            for effect in knight["potion"]["effect"]:
                knight[effect] += knight["potion"]["effect"][effect]

    def fight_lancelot_mordred(self) -> None:
        lancelot = self.knights["lancelot"]
        mordred = self.knights["mordred"]

        lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        mordred["hp"] -= lancelot["power"] - mordred["protection"]

        if lancelot["hp"] <= 0:
            lancelot["hp"] = 0

        if mordred["hp"] <= 0:
            mordred["hp"] = 0

    def fight_arthur_red_knight(self) -> None:
        arthur = self.knights["arthur"]
        red_knight = self.knights["red_knight"]

        arthur["hp"] -= red_knight["power"] - arthur["protection"]
        red_knight["hp"] -= arthur["power"] - red_knight["protection"]

        if arthur["hp"] <= 0:
            arthur["hp"] = 0

        if red_knight["hp"] <= 0:
            red_knight["hp"] = 0

    def start_game(self) -> dict:
        for knight in self.knights:
            self.calculate_knight_protection(knight)
            self.calculate_knight_power(knight)
            self.use_potion(knight)
        self.fight_lancelot_mordred()
        self.fight_arthur_red_knight()
        return {
            self.knights["lancelot"]["name"]: self.knights["lancelot"]["hp"],
            self.knights["arthur"]["name"]: self.knights["arthur"]["hp"],
            self.knights["mordred"]["name"]: self.knights["mordred"]["hp"],
            self.knights["red_knight"]["name"]:
                self.knights["red_knight"]["hp"],
        }


def battle(knights_config: dict) -> dict:
    knights = Battle(knights_config)
    return Battle.start_game(knights)


if __name__ == "__main__":
    battle(KNIGHTS)
