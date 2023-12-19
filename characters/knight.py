class Knight:
    heroes = {}

    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.power = stats["power"]
        self.hp = stats["hp"]
        self.protection = 0

        Knight.heroes[self.name] = self
        self.apply_equipment(stats)

    def apply_weapon(self, stats: dict) -> None:
        self.power += stats["weapon"]["power"]

    def apply_armour(self, stats: dict) -> None:
        for armour in stats["armour"]:
            self.protection += armour["protection"]

    def apply_potion(self, stats: dict) -> None:
        if stats["potion"]:
            self.power += stats["potion"]["effect"].get("power", 0)
            self.hp += stats["potion"]["effect"].get("hp", 0)
            self.protection += stats["potion"]["effect"].get("protection", 0)

    def apply_equipment(self, stats: dict) -> None:
        self.apply_weapon(stats)
        self.apply_armour(stats)
        self.apply_potion(stats)

    @classmethod
    def fight(cls, warrior_name: str, opponent_name: str) -> None:
        warrior = cls.heroes[warrior_name]
        opponent = cls.heroes[opponent_name]

        warrior.hp = max(0, warrior.hp - (opponent.power - warrior.protection))
        opponent.hp = max(0, opponent.hp - (warrior.power - opponent.protection))

    @classmethod
    def hero_status(cls) -> dict:
        return {name: parameter.hp for name, parameter in cls.heroes.items()}
