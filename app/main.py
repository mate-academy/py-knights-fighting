from app.knight import Knight
from app.armor import Armor
from app.weapon import Weapon
from app.potion import Potion
from app.battle import perform_battle

# Конфігурація лицарів
lancelot_armour = []
lancelot_weapon = Weapon("Metal Sword", 50)
lancelot_potion = None
lancelot = Knight("Lancelot", 35, 100, lancelot_armour, lancelot_weapon, lancelot_potion)

arthur_armour = [
    Armor("helmet", 15),
    Armor("breastplate", 20),
    Armor("boots", 10)
]
arthur_weapon = Weapon("Two-handed Sword", 55)
arthur_potion = None
arthur = Knight("Arthur", 45, 75, arthur_armour, arthur_weapon, arthur_potion)

mordred_armour = [
    Armor("breastplate", 15),
    Armor("boots", 10)
]
mordred_weapon = Weapon("Poisoned Sword", 60)
mordred_potion = Potion("Berserk", {"power": +15, "hp": -5, "protection": +10})
mordred = Knight("Mordred", 30, 90, mordred_armour, mordred_weapon, mordred_potion)

red_knight_armour = [
    Armor("breastplate", 25)
]
red_knight_weapon = Weapon("Sword", 45)
red_knight_potion = Potion("Blessing", {"hp": +10, "power": +5})
red_knight = Knight("Red Knight", 40, 70, red_knight_armour, red_knight_weapon, red_knight_potion)

knights = {
    "lancelot": lancelot,
    "arthur": arthur,
    "mordred": mordred,
    "red_knight": red_knight
}

# Виклик функції для битви
knights_list = list(knights.values())
battle_result = perform_battle(knights_list)
print(battle_result)