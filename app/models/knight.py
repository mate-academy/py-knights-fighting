class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.power = 0
        self.protection = 0
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self):
        """Apply the armour protection."""
        self.protection = sum([a["protection"] for a in self.armour])

    def apply_weapon(self):
        """Apply the weapon power."""
        self.power = self.base_power + self.weapon["power"]

    def apply_potion(self):
        """Apply potion effects."""
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def take_damage(self, damage):
        """Reduce the HP of the knight based on the opponent's power and this knight's protection."""
        self.hp -= max(0, damage - self.protection)
        self.hp = max(0, self.hp)  # Ensure HP doesn't go below 0
