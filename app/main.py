from app.preparation import prepar


class Knights:

    def __init__(self, config: dict):
        self.config = config

    def warriors(self, name: str):
        self[name]["protection"] = 0
        return self[name]


def battle(KNIGHTS):
    for_battle = list()
    lancelot = Knights.warriors(KNIGHTS, 'lancelot')
    for_battle.append(lancelot)
    arthur = Knights.warriors(KNIGHTS, 'arthur')
    for_battle.append(arthur)
    mordred = Knights.warriors(KNIGHTS, 'mordred')
    for_battle.append(mordred)
    red_knight = Knights.warriors(KNIGHTS, 'red_knight')
    for_battle.append(red_knight)
    prepar(for_battle)

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for war in for_battle:
        if war['hp'] <= 0:
            war['hp'] = 0

    return {
        KNIGHTS["lancelot"]["name"]: KNIGHTS["lancelot"]["hp"],
        KNIGHTS["arthur"]["name"]: KNIGHTS["arthur"]["hp"],
        KNIGHTS["mordred"]["name"]: KNIGHTS["mordred"]["hp"],
        KNIGHTS["red_knight"]["name"]: KNIGHTS["red_knight"]["hp"],
    }
