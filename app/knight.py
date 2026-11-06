class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        armour: list,
        weapon: dict,
        potion: dict | None
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.prepare_for_battle()

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        return cls(
            name=config["name"],
            hp=config["hp"],
            power=config["power"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )

    def prepare_for_battle(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)

    def fight(self, opponent: "Knight") -> None:
        damage = opponent.power - self.protection
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0


def duel(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.fight(second_knight)
    second_knight.fight(first_knight)
