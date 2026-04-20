class Knight:
    def __init__(self, raw: dict) -> None:
        self.raw = raw or {}
        self.name = self.raw.get("name", "")
        self.hp = int(self.raw.get("hp", 0))
        self.power = int(self.raw.get("power", 0))
        self.protection = int(self.raw.get("protection", 0))
        self.prepared = False

    def apply_armor(self) -> None:
        items = (self.raw.get("armour") or [])
        total_protection = 0
        for part in items:
            total_protection += int(part.get("protection", 0))
        self.protection = self.protection + total_protection

    def apply_weapon(self) -> None:
        weapon = self.raw.get("weapon") or {}
        weapon_power = int(weapon.get("power", 0))
        self.power = self.power + weapon_power

    def apply_potion(self) -> None:
        potion = self.raw.get("potion") or {}
        effect = potion.get("effect") or {}
        self.hp += int(effect.get("hp", 0))
        self.power += int(effect.get("power", 0))
        self.protection += int(effect.get("protection", 0))

    def prepare(self) -> None:
        if getattr(self, "prepared", False):
            return
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()
        self.prepared = True

    def receive_damage(self, dmg: int) -> int:
        actual = max(int(dmg), 0)
        self.hp = max(int(self.hp) - actual, 0)
        return int(self.hp)
