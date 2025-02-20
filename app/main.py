from knights_date import KNIGHTS


class BattleSimulation:
    def __init__(self, knights: KNIGHTS) -> None:
        self.knights = knights

    def knights_preparations(self) -> None:
        for knight in self.knights.values():
            # apply armour
            knight["protection"] = sum([armor["protection"]
                                        for armor in knight["armour"]])

            # apply weapon
            knight["power"] += knight["weapon"]["power"]

            # apply potion if exist
            if knight["potion"]:
                effects = knight["potion"]["effect"]
                knight["power"] += effects.get("power", 0)
                knight["hp"] += effects.get("hp", 0)
                knight["protection"] += effects.get("protection", 0)

    @staticmethod
    def knights_battle(knight1: dict, knight2: dict) -> dict:
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]
        return knight1 if knight1["hp"] > knight2["hp"] else knight2

    def battle_tour(self) -> str:
        self.knights_preparations()
        knights_list = list(self.knights.values())

        while len(knights_list) > 1:
            next_round = []
            for i in range(0, len(knights_list), 2):
                if i + 1 < len(knights_list):
                    winner = self.knights_battle(knights_list[i],
                                                 knights_list[i + 1])
                    next_round.append(winner)
                else:
                    next_round.append(knights_list[i])
            knights_list = next_round
        return knights_list[0]["name"].upper()


battle = BattleSimulation(KNIGHTS)
print(f"THE BATTLE WINNER IS {battle.battle_tour()}")