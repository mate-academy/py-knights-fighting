"""
here is only a fraction of my true power!!!
"""
import time
from app.human.squire import Squire
from app.human.knight import Knight
from app.equipment_data.lancelot_data import LancelotData
from app.equipment_data.arthur_data import ArthurData
from app.equipment_data.mordred_data import MordredData
from app.equipment_data.red_knight_data import RedKnightData


class God:
    @staticmethod
    def bless_method():
        print("God bless you")

    @staticmethod
    def arise_servant(servant_name: str):
        print("Arise!!!")
        if servant_name == "Lancelot's_squire":
            squire = Squire(
                armor_list=LancelotData.ARMOR_LIST,
                weapon=LancelotData.WEAPON
            )
            time.sleep(2)
            print("Lancelot's_squire has arrived!!!")
            return squire
        elif servant_name == "arthur's_squire":
            squire = Squire(
                armor_list=ArthurData.ARMOR_LIST,
                weapon=ArthurData.WEAPON
            )
            time.sleep(2)
            print("arthur's_squire has arrived!!!")
            return squire
        elif servant_name == "mordred's_squire":
            squire = Squire(
                armor_list=MordredData.ARMOR_LIST,
                weapon=MordredData.WEAPON
            )
            squire.potion = Knight.Potion(
                name="Berserk",
                effects=dict(power=+15, hp=-5, protection=+10)
            )
            time.sleep(2)
            print("mordred's_squire has arrived!!!")
            return squire
        elif servant_name == "red_knight's_squire":
            squire = Squire(
                armor_list=RedKnightData.ARMOR_LIST,
                weapon=RedKnightData.WEAPON
            )
            squire.potion = Knight.Potion(
                name="Blessing",
                effects=dict(power=+5, hp=+10)
            )
            time.sleep(2)
            print("red_knight's_squire has arrived!!!")
            return squire
