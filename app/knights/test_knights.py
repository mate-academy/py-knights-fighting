import pytest
from knights.knight import Knight
from knights.weapon import Weapon
from knights.armour import Armour
from knights.potion import Potion

def test_knight_creation():
    weapon = Weapon("Sword", 10)
    armour = [Armour("Helmet", 5), Armour("Chestplate", 15)]
    potion = Potion("Healing Potion", {"hp": 20})
    knight = Knight("Lancelot", 50, 100, armour, weapon, potion)

    assert knight.name == "Lancelot"
    assert knight.power == 50
    assert knight.hp == 100
    assert knight.armour == armour
    assert knight.weapon == weapon
    assert knight.potion == potion
    assert knight.potion_protection == 0

def test_knight_attack():
    weapon1 = Weapon("Sword", 10)
    armour1 = [Armour("Helmet", 5)]
    knight1 = Knight("Lancelot", 50, 100, armour1, weapon1, None)

    weapon2 = Weapon("Axe", 5)
    armour2 = [Armour("Shield", 10)]
    knight2 = Knight("Mordred", 40, 80, armour2, weapon2, None)

    knight1.attack(knight2)
    assert knight2.hp == 45  # 80 - (50 + 10 - 10)

def test_knight_apply_potion():
    potion = Potion("Healing Potion", {"hp": 20, "power": 10, "protection": 5})
    knight = Knight("Arthur", 60, 90, [Armour("Boots", 2)], Weapon("Spear", 15), potion)
    knight.apply_potion()

    assert knight.hp == 110  # 90 + 20
    assert knight.power == 85 # 60 + 15 + 10
    assert knight.protection == 7 # 2 + 5

def test_weapon_creation():
    weapon = Weapon("Axe", 15)
    assert weapon.name == "Axe"
    assert weapon.power == 15

def test_armour_creation():
    armour = Armour("Helmet", 8)
    assert armour.part == "Helmet"
    assert armour.protection == 8

def test_potion_creation():
    potion = Potion("Strength Potion", {"power": 25})
    assert potion.name == "Strength Potion"
    assert potion.effect == {"power": 25}