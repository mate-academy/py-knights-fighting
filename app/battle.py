from app.knights.knight import Knight


class Hero:
    def __init__(self, knight: Knight):
        self.hp = knight.full_hp()
        self.power = knight.full_power()
        self.protection = knight.full_protection()


class Battle:
    def __init__(self, knights: dict):
        self.heroes = {}

        for knight in Knight.knight_list(knights):
            self.heroes[knight.name] = Hero(knight)

    def battle(self, hero1: str, hero2: str):
        if hero1 not in self.heroes:
            print(f"Hero '{hero1}' not found")
            return

        if hero2 not in self.heroes:
            print(f"Hero '{hero2}' not found")
            return

        hero1 = self.heroes[hero1]
        hero2 = self.heroes[hero2]

        hero1.hp -= hero2.power - hero1.protection
        if hero1.hp < 0:
            hero1.hp = 0

        hero2.hp -= hero1.power - hero2.protection
        if hero2.hp < 0:
            hero2.hp = 0
