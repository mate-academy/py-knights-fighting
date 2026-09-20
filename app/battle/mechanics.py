from app.models.knight import Knight


class Battle:
    """Battle mechanics between two knights."""

    def __init__(
        self, first_knight: Knight, second_knight: Knight
    ) -> None:
        """Initialize battle with two knights."""
        self.first_knight = first_knight
        self.second_knight = second_knight

    def fight(self) -> None:
        """Execute simultaneous combat, clamping hp to 0 if <= 0."""
        damage_to_first = (
            self.second_knight.power - self.first_knight.protection
        )
        damage_to_second = (
            self.first_knight.power - self.second_knight.protection
        )

        self.first_knight.hp -= damage_to_first
        self.second_knight.hp -= damage_to_second

        if self.first_knight.hp <= 0:
            self.first_knight.hp = 0
        if self.second_knight.hp <= 0:
            self.second_knight.hp = 0
