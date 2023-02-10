from app.knights.knight import Knight
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour


class ReadData:
    @staticmethod
    def create_weapons_arr(knights: dict) -> None:
        for knight in knights:
            weapon_name = knights[knight]["weapon"]["name"]
            weapon_power = knights[knight]["weapon"]["power"]
            Weapon(weapon_name, weapon_power)

    @staticmethod
    def create_potions_arr(knights: dict) -> None:
        for knight in knights:
            if knights[knight]["potion"] is not None:
                potion_hp = 0
                potion_power = 0
                potion_protection = 0
                potion_name = knights[knight]["potion"]["name"]
                if "hp" in knights[knight]["potion"]["effect"]:
                    potion_hp = knights[knight]["potion"]["effect"]["hp"]
                if "power" in knights[knight]["potion"]["effect"]:
                    potion_power = knights[knight]["potion"]["effect"]["power"]
                if "protection" in knights[knight]["potion"]["effect"]:
                    potion_protection = knights[knight]["potion"]["effect"]["protection"]

                Potion(potion_name, potion_hp, potion_power, potion_protection)

    @staticmethod
    def create_armours_arr(knights: dict):
        for knight in knights:
            if knights[knight]["armour"]:
                for armour in knights[knight]["armour"]:
                    armour_name = armour["part"]
                    armour_protection = armour["protection"]

                    Armour(armour_name, armour_protection)

    @staticmethod
    def create_knights_arr(knights: dict):
        for knight in knights:
            knight_name = knights[knight]["name"]
            knight_power = knights[knight]["power"]
            knight_hp = knights[knight]["hp"]
            knight_armour = []
            knight_potion = None
            if knights[knight]["armour"]:
                knight_armour = [Armour.armours_arr[arm["part"]] for arm in knights[knight]["armour"]]
            knight_weapon = Weapon.weapons_arr[knights[knight]["weapon"]["name"]]
            if knights[knight]["potion"]:
                knight_potion = Potion.potions_arr[knights[knight]["potion"]["name"]]

            for index in range(len(knight_armour)):
                for armour in Armour.armours_arr:
                    if knight_armour[index] == Armour.armours_arr[armour].part:
                        knight_armour[index] = Armour.armours_arr[armour]
                        break

            Knight(knight_name, knight_power, knight_hp, knight_armour, knight_weapon, knight_potion)

    @staticmethod
    def read_data_from_dict(knights_data: dict):
        ReadData.create_weapons_arr(knights_data)
        ReadData.create_armours_arr(knights_data)
        ReadData.create_potions_arr(knights_data)
        ReadData.create_knights_arr(knights_data)

