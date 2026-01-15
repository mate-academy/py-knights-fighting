class Battle:

    def __init__(self, player1: object, player2: object,
                 player3: object, player4: object) -> None:
        self.player1_status = player1
        self.player2_status = player2
        self.player3_status = player3
        self.player4_status = player4

    def battls(self) -> dict:
        players = [self.player1_status, self.player2_status,
                   self.player3_status, self.player4_status]
        for index in range(0, len(players), 2):
            attacker = players[index]
            target = players[index + 1]
            damage = max(0, attacker["power"] - target["protection"])
            target["hp"] -= damage
            attacker, target = target, attacker
            damage = max(0, attacker["power"] - target["protection"])
            target["hp"] -= damage
        for player in players:
            if player["hp"] <= 0:
                player["hp"] = 0

        return {f"""{self.player1_status.get("name")}""":
                self.player1_status.get("hp"),
                f"""{self.player3_status.get("name")}""":
                self.player3_status.get("hp"),
                f"""{self.player2_status.get("name")}""":
                self.player2_status.get("hp"),
                f"""{self.player4_status.get("name")}""":
                self.player4_status.get("hp")}
