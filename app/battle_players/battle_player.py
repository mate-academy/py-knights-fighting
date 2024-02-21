class Battle:

    def __init__(self, player1: object, player2: object,
                 player3: object, player4: object) -> None:
        self.player1_status = player1
        self.player2_status = player2
        self.player3_status = player3
        self.player4_status = player4

    def battls(self) -> dict:
        self.player1_status["hp"] \
            -= (self.player2_status["power"]
                - self.player1_status["protection"])

        self.player2_status["hp"] \
            -= (self.player1_status["power"]
                - self.player2_status["protection"])

        self.player3_status["hp"] \
            -= (self.player4_status["power"]
                - self.player3_status["protection"])

        self.player4_status["hp"] \
            -= (self.player3_status["power"]
                - self.player4_status["protection"])

        players = [self.player1_status, self.player2_status,
                   self.player3_status, self.player4_status]
        for i in players:
            if i["hp"] <= 0:
                i["hp"] = 0
        return {f"""{self.player1_status.get("name")}""":
                self.player1_status.get("hp"),
                f"""{self.player3_status.get("name")}""":
                self.player3_status.get("hp"),
                f"""{self.player2_status.get("name")}""":
                self.player2_status.get("hp"),
                f"""{self.player4_status.get("name")}""":
                self.player4_status.get("hp")}
