from app.knight import Knight


class Battle:
    def __init__(self, participant: Knight, opponent: Knight) -> None:
        self.participant = participant
        self.opponent = opponent

    def process(self) -> None:
        self.participant.hp -= (
            self.opponent.power - self.participant.protection
        )
        self.opponent.hp -= (
            self.participant.power - self.opponent.protection
        )

        if self.participant.hp <= 0:
            self.participant.hp = 0
        if self.opponent.hp <= 0:
            self.opponent.hp = 0
