class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list = None,
                 weapon: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon or {}
        self.potion = potion

        self.protection = 0
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()

    def apply_armor(self) -> None:
        """Calculate total protection from armor"""
        self.protection = sum(piece["protection"] for piece in self.armour)

    def apply_weapon(self) -> None:
        """Calculate power gain from weapon"""
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion:
            for stat, effect in self.potion.get("effect", {}).items():
                # Check and apply potion effects to stats
                if stat == "hp":
                    self.hp += effect
                elif stat == "power":
                    self.power += effect
                elif stat == "protection":
                    self.protection += effect

    def receive_damage(self, damage: int) -> None:
        """Apply damage to health and ensure health >= 0"""
        self.hp = max(0, self.hp - damage)
