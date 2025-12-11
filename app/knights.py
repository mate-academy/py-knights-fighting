class Knights:
    def __init__(self, base_hp: int , base_power: int) -> None:
        self.hp = base_hp
        self.base_hp = base_hp
        self.base_power = base_power
        self.power = base_power
        self.protection = 0
        self.armour = []

    def apply_weapon(self, weapon: dict) -> None:
        self.weapon = weapon
        self.power = self.base_power + weapon["power"]

    def apply_armour(self, armour: dict) -> None:
        self.armour = armour
        total = sum(p["protection"] for p in armour)
        self.protection = total

    def apply_potion(self, potion: dict) -> None:

        if not potion:
            return None

        self.potion = potion

        for stat, delta in potion["effect"].items():

            delta = int(delta)

            if stat == "hp":
                self.hp += delta

            elif stat == "power":
                self.power += delta

            elif stat == "protection":
                self.protection += delta

    def take_damage(self, incoming_power: int) -> None:
        damage = max(0, incoming_power - self.protection)
        self.hp = max(0, self.hp - damage)

    def is_alive(self) -> bool:
        return self.hp > 0
