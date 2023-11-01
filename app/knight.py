

class Knight:

    def __init__(self, knight: dict) -> None:
        self.protection = 0
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def take_weapon(self) -> None:
        self.power += self.weapon["power"]

    def put_on_armor(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    def use_potion(self) -> None:
        if self.potion:
            potion_effect = self.potion["effect"]
            for key, value in potion_effect.items():
                if hasattr(self, key):  # Checking if the attribute exists
                    current_value = getattr(self, key)
                    setattr(self, key, current_value + value)

    def get_ready_to_battle(self) -> None:
        self.take_weapon()
        self.put_on_armor()
        self.use_potion()
