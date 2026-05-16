class KnightsConfig:
    def __init__(self, knight : dict) -> None:
        self.knight = knight

    def calculate_protection(self) -> int:
        protection = 0
        potion = self.knight.get("potion")
        for atr in self.knight["armour"]:
            protection += atr["protection"]
        if potion and potion.get("effect"):
            protection += potion["effect"].get("protection", 0)
        return protection

    def calculate_power(self) -> int:
        power = self.knight["power"] + self.knight["weapon"]["power"]
        potion = self.knight.get("potion")
        if potion and potion.get("effect"):
            power += potion["effect"].get("power", 0)
        return power

    def calculate_hp(self) -> int:
        hp = self.knight["hp"]
        potion = self.knight.get("potion")
        if potion and potion.get("effect"):
            hp += potion["effect"].get("hp", 0)
        return hp


def fight(knight1_data: dict, knight2_data: dict) -> tuple[int, int]:
    k1 = KnightsConfig(knight1_data)
    k2 = KnightsConfig(knight2_data)

    def calc_final_hp(atkr: KnightsConfig, dfdr: KnightsConfig) -> int:
        damage = max(0, atkr.calculate_power() - dfdr.calculate_protection())
        return max(0, dfdr.calculate_hp() - damage)

    hp1 = calc_final_hp(k2, k1)
    hp2 = calc_final_hp(k1, k2)

    return hp1, hp2


def battle(knights: dict) -> dict:
    lancelot_hp, mordred_hp = fight(knights["lancelot"], knights["mordred"])
    arthur_hp, red_knight_hp = fight(knights["arthur"], knights["red_knight"])

    return {"Lancelot" : lancelot_hp,
            "Mordred" : mordred_hp,
            "Arthur" : arthur_hp,
            "Red Knight" : red_knight_hp}
