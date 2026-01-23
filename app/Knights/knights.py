from app.Knights.armor import Armor


class Knight:
    def __init__(self, name: str, power: int, hp: int, protection: int):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection



"""
ідкя наступна: створити перед боєм лицарів а потім рахувати переможця
тообто кожен клас предметів просто повертає значення які потім буде використано для створення ліцаря
потім бій і оголошення результатів згідно вімог тестів

увесь бій зводиться до формули hp(red) -= power(blue) - protection(red) 
а щоб дійти доцього треба рахувати стати лицарів перед боєм
"""


