from app.knights.knight import Knight


class Battle:
    def __init__(self, participants: list[Knight]):
        self.participants = [participant for participant in participants]

    