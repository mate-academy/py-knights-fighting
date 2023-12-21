class Battle:

    def __init__(self, opponent_1: str,
                 opponent_2: str, king_conf: dict) -> None:
        self.opponent_1 = opponent_1
        self.opponent_2 = opponent_2
        self.king_conf = king_conf

    def battle_opponent(self) -> dict:
        lancelot = self.king_conf[self.opponent_1]
        mordred = self.king_conf[self.opponent_2]
        lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        mordred["hp"] -= lancelot["power"] - mordred["protection"]

        # check if someone fell in battle
        if lancelot["hp"] <= 0:
            lancelot["hp"] = 0

        if mordred["hp"] <= 0:
            mordred["hp"] = 0

        # Upgrade the dict with new data
        self.king_conf[lancelot["name"]] = lancelot
        self.king_conf[mordred["name"]] = mordred

        return self.king_conf
