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

        self.check_hp(self.participant)
        self.check_hp(self.opponent)

    @staticmethod
    def check_hp(knight: Knight) -> None:
        if knight.hp < 0:
            knight.hp = 0
