class Potion:
    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0,
    ):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def create_potion(potion_dict):
        name = potion_dict['name']
        power = 0
        hp = 0
        protection = 0
        effects = potion_dict['effect']

        if 'power' in effects:
            power = effects['power']
        if 'hp' in effects:
            hp = effects['hp']
        if 'protection' in effects:
            protection = effects['protection']

        return Potion(
            name=name,
            power=power,
            hp=hp,
            protection=protection,
        )
