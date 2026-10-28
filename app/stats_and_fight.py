class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.armour = data.get("armour", [])
        self.weapon = data.get("weapon", {})
        self.potion = data.get("potion")

    def calculate_stats(self) -> dict:
        protection = sum(item["protection"] for item in self.armour)
        power = self.power + self.weapon.get("power", 0)
        hp = self.hp
        if self.potion:
            effect = self.potion.get("effect", {})
            hp += effect.get("hp", 0)
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)
        return {
            "name": self.name,
            "hp": hp,
            "power": power,
            "protection": protection,
        }

    def fight(self, opponent: "Knight") -> None:
        my_stats = self.calculate_stats()
        opp_stats = opponent.calculate_stats()

        damage_to_me = max(0, opp_stats["power"] - my_stats["protection"])
        damage_to_opp = max(0, my_stats["power"] - opp_stats["protection"])

        self.hp = max(0, my_stats["hp"] - damage_to_me)
        opponent.hp = max(0, opp_stats["hp"] - damage_to_opp)
