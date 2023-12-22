class Competition:

    @staticmethod
    def battle_opponent(opponent_1: str,
                        opponent_2: str, king_conf: dict) -> dict:
        first = king_conf[opponent_1]
        second = king_conf[opponent_2]
        first["hp"] -= second["power"] - first["protection"]
        second["hp"] -= first["power"] - second["protection"]

        # check if someone fell in battle
        if first["hp"] <= 0:
            first["hp"] = 0

        if second["hp"] <= 0:
            second["hp"] = 0

        # Upgrade the dict with new data
        king_conf[first["name"]] = first
        king_conf[second["name"]] = second

        return king_conf

    @staticmethod
    def result_of_tournament(kings: dict) -> dict:
        return {name: conf_info["hp"] for name, conf_info in kings.items()}
