class Battle:

    def __init__(self):
        pass

    @staticmethod
    def get_in_order(knights):
        lst = []
        for pers in knights.values():
            lst.append(pers)
        lst1 = lst[:len(lst) // 2]
        lst2 = lst[len(lst) // 2:]
        order = list(zip(lst1, lst2))
        return order

    @staticmethod
    def fighting(knights: tuple):
        knights[0].hp -= knights[1].power - knights[0].protection
        knights[1].hp -= knights[0].power - knights[1].protection
