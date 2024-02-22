class Battle:

    def __init__(self, player1: object, player2: object,
                 player3: object, player4: object) -> None:
        self.player_lancelot_status = player1
        self.player_arthur_status = player2
        self.player_mordred_status = player3
        self.player_red_knight_status = player4

    def battls(self) -> dict:

        players = [self.player_lancelot_status, self.player_arthur_status,
                   self.player_mordred_status, self.player_red_knight_status]

        for index in range(0, len(players), 2):
            attacker = players[index]
            target = players[index + 1]
            for _ in range(2):
                damage = max(0, attacker["power"] - target["protection"])
                target["hp"] -= damage
                attacker, target = target, attacker

        for player in players:
            if player["hp"] <= 0:
                player["hp"] = 0

        return {player.get("name"): player.get("hp") for player in players}
