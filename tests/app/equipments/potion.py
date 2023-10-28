class Potion:

    def __init__(self, knight_name: str, potion: dict) -> None:
        self.potion = potion
        self.knight_name = knight_name

    def __iadd__(self, knight: callable) -> None:
        """
        calculates and change main properties for instances class
        :param knight: instance class Knights
        :return: None
        """
        for effect, value in self.potion.items():
            if self.knight_name in knight.name and effect:
                if effect in "hp":
                    knight.hp += value
                if effect in "power":
                    knight.power += value
                if effect in "protection":
                    knight.protection += value
