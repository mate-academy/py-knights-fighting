class Knights:
    # This constructor is creating a knight (Knights class instance),
    # which is ready for the battle
    # (armoured and potion applied (if available)).
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: list,
            weapon: dict,
            potion: dict | None) -> None:
        self.name = name
        self.hp = hp
        self.protection = 0
        if armour:
            for item in armour:
                self.protection += item.get("protection")
        extra_power = 0
        if potion:
            self.hp = hp + potion.get("effect").get("hp")
            extra_power = potion.get("effect").get("power")
            if potion.get("effect").get("protection"):
                self.protection += potion.get("effect").get("protection")
        self.power = power + extra_power + weapon.get("power")

    # module is simulating fight between two knights (class instances)
    def fight(self, other: "Knights") -> None:
        hp_self = self.hp - other.power + self.protection
        hp_other = other.hp - self.power + other.protection
        if hp_self <= 0:
            self.hp = 0
        else:
            self.hp = hp_self
        if hp_other <= 0:
            other.hp = 0
        else:
            other.hp = hp_other
