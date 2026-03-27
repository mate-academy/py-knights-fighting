class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for piece in self.armour:
            self.protection += piece["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]
# -----------------------BATTLE--------------------------------

    def take_damage(self, damage: int) -> None:
        effective_damage = damage - self.protection
        if effective_damage > 0:
            self.hp -= effective_damage
        if self.hp < 0:
            self.hp = 0


def battle(knights: dict) -> dict:
    # Create Knight objects
    lancelot = Knight(**knights["lancelot"])
    arthur = Knight(**knights["arthur"])
    mordred = Knight(**knights["mordred"])
    red_knight = Knight(**knights["red_knight"])

    # 1 Lancelot vs Mordred
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # 2 Arthur vs Red Knight
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # Return battle results
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
