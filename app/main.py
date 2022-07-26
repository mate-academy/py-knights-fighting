from app.startStats import KNIGHTS


class King:
    def __init__(self, name, power, hp, protection=0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def new_stat(self, name):
        for armour in name["armour"]:
            self.protection += armour["protection"]

        # apply weapon
        self.power += name["weapon"]["power"]

        # apply potion if exist
        stats = ("protection", "power", "hp")
        if name["potion"] is not None:
            effect = name["potion"]["effect"]
            for stat in stats:
                if stat in effect:
                    setattr(self, stat, getattr(self, stat) + effect[stat])

    def __sub__(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0


def battle(knightsConfig):
    knights = {}
    for key, value in knightsConfig.items():
        knights[value['name']] = King(
            value['name'],
            value['power'],
            value['hp'])

    knights["Lancelot"].new_stat(knightsConfig["lancelot"])
    knights["Artur"].new_stat(knightsConfig["arthur"])
    knights["Mordred"].new_stat(knightsConfig["mordred"])
    knights["Red Knight"].new_stat(knightsConfig["red_knight"])

    knights["Lancelot"] - knights["Mordred"]
    knights["Artur"] - knights["Red Knight"]

    return {
        knights["Lancelot"].name: knights["Lancelot"].hp,
        knights["Artur"].name: knights["Artur"].hp,
        knights["Mordred"].name: knights["Mordred"].hp,
        knights["Red Knight"].name: knights["Red Knight"].hp
    }


print(battle(KNIGHTS))
