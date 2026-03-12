from app.battle_knight.knight_for_battle import KnightForBattle


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.battle_hp = hp
        self.battle_power = power
        self.battle_protection = 0

    @classmethod
    def new_knight(cls, knight_dict: dict) -> Knight:
        return cls(
            **knight_dict
        )

    def apply_armour(self) -> None:
        for part in self.armour:
            self.battle_protection += part["protection"]

    def apply_weapon(self) -> None:
        self.battle_power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion.get("effect", None)
            if isinstance(effect, dict):
                self.battle_hp += effect.get("hp", 0)
                self.battle_power += effect.get("power", 0)
                self.battle_protection += effect.get("protection", 0)

    def before_battle(self) -> None:
        self.battle_hp = self.hp
        self.battle_power = self.power
        self.battle_protection = 0

    def prepare_for_battle(self) -> KnightForBattle:
        self.before_battle()
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

        return KnightForBattle(
            self.name,
            self.battle_hp,
            self.battle_power,
            self.battle_protection
        )
