class Battle:
    def __init__(self):
        pass

    @staticmethod
    def fight(first: dict, second: dict):
        name_first = list(first.keys())[0]
        name_second = list(second.keys())[0]

        # BATTLE
        first[name_first]["hp"] -= \
            second[name_second]["power"] - first[name_first]["protection"]

        second[name_second]["hp"] -= \
            first[name_first]["power"] - second[name_second]["protection"]

        # check if someone fell in battle
        if first[name_first]["hp"] <= 0:
            first[name_first]["hp"] = 0

        if second[name_second]["hp"] <= 0:
            second[name_second]["hp"] = 0

        # Return battle results:
        return {
            first[name_first]["name"]: first[name_first]["hp"],
            second[name_second]["name"]: second[name_second]["hp"],
        }
