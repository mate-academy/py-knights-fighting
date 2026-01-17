class Competition:

    @staticmethod
    def battle_opponent(opponent_1: dict, opponent_2: dict) -> dict:
        king_conf = {}
        opponent_1["hp"] -= opponent_2["power"] - opponent_1["protection"]
        opponent_2["hp"] -= opponent_1["power"] - opponent_2["protection"]

        # check if someone fell in battle
        if opponent_1["hp"] <= 0:
            opponent_1["hp"] = 0

        if opponent_2["hp"] <= 0:
            opponent_2["hp"] = 0

        # Upgrade the dict with new data
        king_conf[opponent_1["name"]] = opponent_1
        king_conf[opponent_2["name"]] = opponent_2

        return king_conf

    @staticmethod
    def result_of_tournament(kings: dict) -> dict:
        return {name: conf_info["hp"] for name, conf_info in kings.items()}
