class Knight:
    knights = {}

    def __init__(
            self,
            knight_config: dict
    ) -> None:
        for skill, skill_value in knight_config.items():
            setattr(self, skill, skill_value)
        self.protection = 0
        Knight.knights[self.name] = self

    def get_ready_to_fight(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            effect = self.potion["effect"]
            for add_skill in ("power", "hp", "protection"):
                if add_skill in effect:
                    current_value = getattr(self, add_skill)
                    setattr(self, add_skill, current_value + effect[add_skill])


def create_knights(knights: dict) -> dict:
    for knight in knights:
        Knight(knights[knight])
    return Knight.knights
