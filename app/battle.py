from app.knight import Knight


class Battle:
    def __init__(self, knights: dict) -> None:
        self.knights = {
            name: Knight(
                name=knight["name"],
                power=knight["power"],
                hp=knight["hp"],
                armour=knight["armour"],
                weapon=knight["weapon"],
                potion=knight["potion"]
            )
            for name, knight in knights.items()
        }

    def apply_knight_modifiers(self) -> None:
        for knight in self.knights.values():
            knight.apply_armour()
            knight.apply_weapon()
            knight.apply_potion()

    def fight(self) -> dict:
        self.knights["lancelot"].hp -= \
            self.knights["mordred"].power - \
            self.knights["lancelot"].protection
        self.knights["mordred"].hp -= \
            self.knights["lancelot"].power - \
            self.knights["mordred"].protection

        self.knights["arthur"].hp -= \
            self.knights["red_knight"].power - \
            self.knights["arthur"].protection
        self.knights["red_knight"].hp -= \
            self.knights["arthur"].power - \
            self.knights["red_knight"].protection

        # Ensure HP is non-negative
        for knight in self.knights.values():
            if knight.hp <= 0:
                knight.hp = 0

        # Return battle results as a dictionary
        return {knight.name: knight.hp for knight in self.knights.values()}
