from app.knights.knights import Knights
from app.knights.equipment.armour import Armour
from app.knights.equipment.potion import Potion
from app.knights.equipment.weapon import Weapon

lancelot_weapon = Weapon("Metal Sword", 50)
lancelot_armour = []
lancelot_potion = Potion()
lancelot_it = Knights(name = "lancelot",
                   name_knight= "Lancelot",
                   power = 35,
                   hp = 100,
                   armour = lancelot_armour,
                   weapon = lancelot_weapon,
                   potion = lancelot_potion)

arthur_weapon = Weapon("Two-handed Sword", 55)
arthur_armour_1 = Armour("helmet", 15)
arthur_armour_2 = Armour("breastplate", 20)
arthur_armour_3 = Armour("boots", 10)
arthur_armour = [arthur_armour_1,
                 arthur_armour_2,
                 arthur_armour_3]
arthur_potion = Potion()
arthur_it = Knights(name = "arthur",
                 name_knight= "Arthur",
                 power = 45,
                 hp = 75,
                 armour = arthur_armour,
                 weapon = arthur_weapon,
                 potion = arthur_potion)

mordred_weapon = Weapon("Poisoned Sword", 60)
mordred_armour_1 = Armour("breastplate", 15)
mordred_armour_2 = Armour("boots", 10)
mordred_armour = [mordred_armour_1, mordred_armour_2]
mordred_potion = Potion("Berserk", 15, -5, 10)
mordred_it = Knights(name = "mordred",
                  name_knight= "Mordred",
                  power = 90,
                  hp = 30,
                  armour = mordred_armour,
                  weapon = mordred_weapon,
                  potion = mordred_potion)

red_knight_weapon = Weapon("Sword", 45)
red_knight_armour_1 = Armour("breastplate", 25)
red_knight_armour = [red_knight_armour_1]
red_knight_potion = Potion("Blessing", 10, 5)
red_knight_it = Knights(name = "red_knight",
                     name_knight = "Red Knight",
                     power = 40,
                     hp = 70,
                     armour = red_knight_armour,
                     weapon = red_knight_weapon,
                     potion = red_knight_potion)

