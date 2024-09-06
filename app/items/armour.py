class Armour:
    """
    Represents an armour piece worn by a knight. Armour provides protection
    during battles, reducing the damage taken by the knight.

    Attributes:
        part (str): The part of the knight's body that the armour protects
                    (e.g., breastplate, helmet).
        protection (int): The protection value of the armour piece.
    """

    def __init__(self, part: str, protection: int) -> None:
        """
        Initializes an armour piece with the part of the body
        it protects and the amount of protection it provides.

        Args:
            part (str): The name of the armour piece
                        (e.g., breastplate, helmet).
            protection (int):
                The protection value that reduces damage in battle.
        """
        self.part = part
        self.protection = protection
