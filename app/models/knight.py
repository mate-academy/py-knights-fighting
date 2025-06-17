class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: dict = None) -> None:
        self.name = name
        self.base_power = power
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(a.get("protection", 0) for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if not self.potion:
            return
        effect = self.potion.get("effect", {})
        self.power += effect.get("power", 0)
        self.hp += effect.get("hp", 0)
        self.protection += effect.get("protection", 0)

    def prepare_for_battle(self) -> object:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self

    def receive_damage(self, raw_damage: int) -> None:
        damage = max(0, raw_damage)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
