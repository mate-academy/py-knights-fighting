from app.tournament.round import Round


class Battle:

    def __init__(self, knights: dict) -> None:
        self.knights = knights

    def start_fight(self) -> dict:
        Round(self.knights["lancelot"], self.knights["mordred"]).round()
        Round(self.knights["arthur"], self.knights["red_knight"]).round()

        return {
            self.knights["lancelot"].name:
                self.knights["lancelot"].hp,
            self.knights["arthur"].name:
                self.knights["arthur"].hp,
            self.knights["mordred"].name:
                self.knights["mordred"].hp,
            self.knights["red_knight"].name:
                self.knights["red_knight"].hp,
        }
