from app.knights.knight import Knight
from app.armours.armour import Armour
from app.weapons.weapon import Weapon
from app.weapons.potions.potion import Potion
from app.battle.battle import Battle

# BATTLE PREPARATIONS:

lancelot = Knight('lancelot', 35, 100)
metal_sword = Weapon("Metal-sword", 50)
lancelot.take_weapon(metal_sword)

# arthur
arthur = Knight("arthur", 45, 75)
two_handed_sword = Weapon("Two-handed Sword", 55)
helmet = Armour("helmet", 15)
breastplate = Armour("breastplate", 20)
boots = Armour("boots", 10)
arthur.take_weapon(two_handed_sword)
arthur.put_on_armour(helmet)
arthur.put_on_armour(breastplate)
arthur.put_on_armour(boots)

# mordred
mordred = Knight("mordred", 30, 90)
breastplate = Armour("breastplate", 15)
poisoned_sword = Weapon("Poisoned Sword", 60)
berserk = Potion("Berserk", 15, 10, -5)

mordred.take_weapon(poisoned_sword)
mordred.put_on_armour(boots)
mordred.put_on_armour(breastplate)
mordred.take_potion(berserk)

# red_knight
red_knight = Knight("Red-knight", 40, 70)
breastplate = Armour("breastplate", 25)
sword = Weapon("Sword", 45)
blessing = Potion("blessing", 5, 0, 10)

red_knight.put_on_armour(breastplate)
red_knight.take_weapon(sword)
red_knight.take_potion(blessing)

# -------------------------------------------------------------------------------
# BATTLE:

# 1 Lancelot vs Mordred:
# BATTLE: 1
first_battle = Battle(lancelot, mordred)
first_battle.start_battle()

# 2 Arthur vs Red Knight:
second_battle = Battle(arthur, red_knight)
second_battle.start_battle()

# Return battle results:


print({
    lancelot.name: lancelot.hp,
    arthur.name: arthur.hp,
    mordred.name: mordred.hp,
    red_knight.name: red_knight.hp,
})
