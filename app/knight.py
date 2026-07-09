class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]
        self.protection = 0

    def apply_preparations(self) -> None:
        for piece in self.armour:
            self.protection += piece["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def fight(self, opponent: "Knight") -> None:
        damage_to_me = opponent.power - self.protection
        damage_to_opponent = self.power - opponent.protection
        self.hp -= damage_to_me
        opponent.hp -= damage_to_opponent

        if self.hp < 0:
            self.hp = 0
        if opponent.hp < 0:
            opponent.hp = 0
