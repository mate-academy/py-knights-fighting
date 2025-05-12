from app.game.heroes import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def prepare_battle(self) -> None:
        # Apply armor
        self.first_knight.apply_armour()
        self.second_knight.apply_armour()
        # Apply weapon
        self.first_knight.apply_weapon()
        self.second_knight.apply_weapon()
        # Apply potion if exist
        self.first_knight.apply_potion()
        self.second_knight.apply_potion()

    def fight(self) -> None:
        self.prepare_battle()  # Prepare before battle

        self.first_knight.hp -= max(
            0, self.second_knight.power - self.first_knight.protection
        )
        self.second_knight.hp -= max(
            0, self.first_knight.power - self.second_knight.protection
        )

        if self.first_knight.hp < 0:
            self.first_knight.hp = 0
        if self.second_knight.hp < 0:
            self.second_knight.hp = 0
