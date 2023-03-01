class Potion():

    def __init__(self, name: str, power: int = 0,
                 hp: int = 0, protection: int = 0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def create_potion(potion: dict):
        if potion:
            effects = potion["effect"]
            power, hp, protection = 0, 0, 0
            if 'power' in effects:
                power = effects['power']
            if 'hp' in effects:
                hp = effects['hp']
            if 'protection' in effects:
                protection = effects['protection']
            return Potion(potion["name"], power=power,
                          hp=hp, protection=protection)
        return
