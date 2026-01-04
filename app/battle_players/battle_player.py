class Battle:

    def __init__(self, states: list) -> None:
        for state in states:

            if state.get("name") == "Lancelot":
                self.player_lancelot_status = state

            elif state.get("name") == "Arthur":
                self.player_arthur_status = state

            elif state.get("name") == "Mordred":
                self.player_mordred_status = state

            elif state.get("name") == "Red Knight":
                self.player_red_knight_status = state

    def battls(self) -> dict:

        players = [self.player_lancelot_status, self.player_arthur_status,
                   self.player_mordred_status, self.player_red_knight_status]

        for index in range(0, len(players) - 2):
            attacker = players[index]
            target = players[index + 2]
            for _ in range(2):
                damage = max(0, attacker["power"] - target["protection"])
                target["hp"] -= damage
                attacker, target = target, attacker

        for player in players:
            if player["hp"] <= 0:
                player["hp"] = 0

        return {player.get("name"): player.get("hp") for player in players}
