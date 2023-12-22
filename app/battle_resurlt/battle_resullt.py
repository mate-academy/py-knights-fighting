class Competition:

    @staticmethod
    def battle_opponent(opponent_1: str,
                        opponent_2: str, king_conf: dict) -> dict:
        lancelot = king_conf[opponent_1]
        mordred = king_conf[opponent_2]
        lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        mordred["hp"] -= lancelot["power"] - mordred["protection"]

        # check if someone fell in battle
        if lancelot["hp"] <= 0:
            lancelot["hp"] = 0

        if mordred["hp"] <= 0:
            mordred["hp"] = 0

        # Upgrade the dict with new data
        king_conf[lancelot["name"]] = lancelot
        king_conf[mordred["name"]] = mordred

        return king_conf

    @staticmethod
    def result_of_tournament(kings: dict) -> dict:
        return {x: y["hp"] for x, y in kings.items()}
