class Knights:

    knights_list = []

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.weapon = knight["weapon"]
        self.armour = knight["armour"]
        self.potion = knight["potion"]
        self.all_defence = 0
        Knights.knights_list.append(self)

    def take_weapon(self, weapon: dict) -> None:

        self.power += weapon.get("power", 0)

    def take_armour(self, armours: dict) -> None:

        for armour in armours:
            self.all_defence += armour.get("protection", 0)

    def take_pontions(self, pontions: dict) -> None:

        if pontions is not None:
            self.hp += pontions["effect"].get("hp", 0)
            self.power += pontions["effect"].get("power", 0)
            self.all_defence += pontions["effect"].get("protection", 0)

    def prepare_to_fight(self) -> None:

        self.take_armour(self.armour)
        self.take_pontions(self.potion)
        self.take_weapon(self.weapon)
