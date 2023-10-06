class Armour:

    def __init__(self, part: str, protect: int) -> None:
        self.part = part
        self.protect = protect

    def __str__(self) -> str:
        return f"part: {self.part}, protect: {self.protect}"
