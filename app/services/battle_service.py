class BattleService:
    def __init__(self) -> None:
        pass

    def duel(self, knight1: dict, knight2: dict) -> (dict, dict):
        stats1 = knight1.get_battle_stats()
        stats2 = knight2.get_battle_stats()
        damage_to_knight1 = max(0, stats2["power"] - stats1["protection"])
        damage_to_knight2 = max(0, stats1["power"] - stats2["protection"])
        hp1_after = max(0, stats1["hp"] - damage_to_knight1)
        hp2_after = max(0, stats2["hp"] - damage_to_knight2)
        return {
            "name": stats1["name"],
            "hp": hp1_after
        }, {
            "name": stats2["name"],
            "hp": hp2_after
        }

    def tournament(self, knights: dict, matchups: list | None = None) -> dict:
        if matchups is None:
            matchups = [("lancelot", "mordred"), ("arthur", "red_knight")]
        results = {}
        for knight1_key, knight2_key in matchups:
            if knight1_key in knights and knight2_key in knights:
                knight1 = knights[knight1_key]
                knight2 = knights[knight2_key]
                result1, result2 = self.duel(knight1, knight2)
                results[result1["name"]] = result1["hp"]
                results[result2["name"]] = result2["hp"]
        return results
