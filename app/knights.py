from app.equipment import Weapon, Armour, Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int, protection=0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def attack_enemy(self, other):
        other.hp -= self.power - other.protection


lancelot = Knight("Lancelot", 35, 100)
lancelot_sword = Weapon("Metal Sword", 50)
lancelot_sword.apply_weapon(lancelot)

arthur = Knight("Artur", 45, 75)
arthur_helmet = Armour("helmet", 15)
arthur_breastplate = Armour("breastplate", 20)
arthur_boots = Armour("boots", 10)
arthur_sword = Weapon("Two-handed Sword", 55)
arthur_helmet.apply_armor(arthur)
arthur_breastplate.apply_armor(arthur)
arthur_boots.apply_armor(arthur)
arthur_sword.apply_weapon(arthur)

mordred = Knight("Mordred", 30, 90)
mordred_breastplate = Armour("breastplate", 15)
mordred_boots = Armour("boots", 10)
mordred_weapon = Weapon("Poisoned Sword", 60)
mordred_potion = Potion("Berserk", {"power": +15,
                                    "hp": -5,
                                    "protection": +10})
mordred_breastplate.apply_armor(mordred)
mordred_boots.apply_armor(mordred)
mordred_weapon.apply_weapon(mordred)
mordred_potion.apply_potion(mordred)


red_knight = Knight("Red Knight", 40, 70)
red_knight_breastplate = Armour("breastplate", 25)
red_knight_weapon = Weapon("Sword", 45)
red_knight_potion = Potion("Blessing", {"hp": +10,
                                        "power": +5})
red_knight_breastplate.apply_armor(red_knight)
red_knight_weapon.apply_weapon(red_knight)
red_knight_potion.apply_potion(red_knight)
