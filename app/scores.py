class Scores:
    knight1 = {}
    knight2 = {}

    @classmethod
    def battle_scores(cls, knight1, knight2) -> dict:
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]
        if knight1["hp"] <= 0:
            knight1["hp"] = 0
            print(f"{knight1['name']} defeated! Congratulations to {knight2['name']}!")
        elif knight2["hp"] <= 0:
            knight2["hp"] = 0
            print(f"{knight2['name']} defeated! Congratulations to {knight1['name']}!")
        return {knight1["name"]: knight1["hp"], knight2["name"]: knight2["hp"]}
