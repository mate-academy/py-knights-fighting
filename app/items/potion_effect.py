class Effect:
    def __init__(self, power: int, hp: int, protection=None) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection


poison_effect = {"effect": {
    "hp": +10,
    "power": +5,
}}
effect = Effect(poison_effect["effect"]["power"], poison_effect["effect"]["hp"])
print(f" hp = {effect.hp}")
print(f" power = {effect.power}")
print(f" protection = {effect.protection}")