from __future__ import annotations


class Knight:
    def __init__(
            self,
            knight_dict: dict
    ) -> None:
        self.name = knight_dict.get("name")
        self.power = knight_dict.get("power")
        self.hp = knight_dict.get("hp")
        self.weapon = knight_dict.get("weapon")
        self.armour = knight_dict.get("armour")
        self.potion = knight_dict.get("potion")
        self.battle_ready_stats = self.battle_ready_stats()

    # calculates battle ready knight's stats
    def battle_ready_stats(self) -> dict:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.hp += self.potion["effect"]["protection"]

        # battle_hp -> sum of hp, armour protection ...
        # ... and(if) potion hp or/and protection
        battle_hp = self.hp + \
            sum([armour["protection"] for armour in self.armour])

        # battle_power -> sum of knight power, weapon power ...
        # ...and (if) potion power
        battle_power = self.power + self.weapon["power"]
        return {"battle_hp": battle_hp, "battle_power": battle_power}

    def fight(self, other: Knight) -> dict:
        hp_left = self.battle_ready_stats["battle_hp"] \
            - other.battle_ready_stats["battle_power"]

        villain_hp_left = other.battle_ready_stats["battle_hp"] \
            - self.battle_ready_stats["battle_power"]

        hp_left = max(0, hp_left)
        villain_hp_left = max(0, villain_hp_left)

        # return dict with after fight knight's stats
        return {
            self.name: hp_left,
            other.name: villain_hp_left
        }
