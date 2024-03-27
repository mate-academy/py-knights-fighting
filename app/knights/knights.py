from time import sleep


class Knight:
    def __init__(self, knights: dict) -> None:
        self.name = knights["name"]
        self.power = knights["power"]
        self.hp = knights["hp"]
        self.armour = knights["armour"]
        self.protection = 0
        self.weapon = knights["weapon"]
        self.potion = knights["potion"]

    def equip_weapon(self) -> None:
        self.power += self.weapon["power"]
        print(f"Knight {self.name} equipped weapon {self.weapon['name']}"
              f"+{self.weapon['power']} points to power.")

    def equip_armour(self) -> None:
        if self.armour:
            self.protection = sum(part_armour["protection"]
                                  for part_armour in self.armour)
            for part in self.armour:
                print(f"Knight {self.name} put on his {part['part']}.")
                sleep(0.3)
            print(f"Total protection +{self.protection} points.")
        else:
            print(f"Knight {repr(self.name)} don't have any armour.")

    def drink_potion(self) -> None:
        if self.potion:
            effects = self.potion["effect"]
            for effect in effects:
                if "power" in effect:
                    self.power += effects["power"]
                if "hp" in effect:
                    self.hp += effects["hp"]
                if "protection" in effect:
                    self.protection += effects["protection"]
            print(f"Knight {self.name} use potion {self.potion['name']}.")

    def knights_battle(self, knight: object) -> None:
        self.hp -= knight.power - self.protection
        knight.hp -= self.power - knight.protection
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} is fell in this battle.")
            print(f"{knight.name} is win in this battle.")
        elif knight.hp <= 0:
            knight.hp = 0
            print(f"{knight.name} is fell in this battle.")
            print(f"{self.name} is win in this battle.")
        else:
            print("Our knights are live, so it`s a draw.")
