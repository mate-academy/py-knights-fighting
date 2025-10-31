from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


if __name__ == "__main__":
    print(Armour([{"part": 1}]))
    print(Weapon("knife", 45))
    print(Potion("fly", {"hp": 999}))
