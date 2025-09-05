class Combatant:
    def __init__(self, source: dict) -> None:
        self.name = source["name"]
        self.power = source["power"]
        self.hp = source["hp"]
        self.protection = 0
        self.apply_armor(source)
        self.apply_weapon(source)
        self.apply_potions(source)

    def apply_armor(self, source: dict) -> None:
        self.protection = sum(item["protection"] for item in source["armour"])
            
    def apply_weapon(self, source: dict) -> None:
        self.power += source["weapon"]["power"]
    
    def apply_potions(self, source: dict) -> None:
        effect = source["potion"].get("effect", {}) if source["potion"] else {}
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)
