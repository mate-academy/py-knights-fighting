class ArmourPiece:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

arthur_breastplate = ArmourPiece("breastplate", 20)
mordred_breastplate = ArmourPiece("breastplate", 15)