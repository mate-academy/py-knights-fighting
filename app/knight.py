class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0
        self.if_prepared = False

    def preparation(self) -> Knight:
        if self.if_prepared:
            return self

        for armour_part in self.armour:
            self.protection += armour_part["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            for key, value in self.potion["effect"].items():
                if key == "hp":
                    self.hp += value
                elif key == "power":
                    self.power += value
                elif key == "protection":
                    self.protection += value
        self.if_prepared = True
        return self

    def fight(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        if self.hp <= 0:
            self.hp = 0
        if enemy.hp <= 0:
            enemy.hp = 0
