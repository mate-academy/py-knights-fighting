class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict,
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0  # Default protection

        self.apply_armour(armour)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def __str__(self) -> str:
        return self.name

    def apply_armour(self, armour: list) -> None:
        for piece in armour:
            self.protection += piece.get("protection", 0)

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power", 0)

    def apply_potion(self, potion: dict) -> None:
        if potion is not None:
            self.hp += potion.get("effect", {}).get("hp", 0)
            self.power += potion.get("effect", {}).get("power", 0)
            self.protection += potion.get("effect", {}).get("protection", 0)

    @staticmethod
    def battle(knight1: "Knight", knight2: "Knight") -> dict:
        knight1_damage = max(0, knight2.power - knight1.protection)
        knight2_damage = max(0, knight1.power - knight2.protection)

        knight1.hp = max(0, knight1.hp - knight1_damage)
        knight2.hp = max(0, knight2.hp - knight2_damage)

        return {knight1.name: knight1.hp, knight2.name: knight2.hp}
