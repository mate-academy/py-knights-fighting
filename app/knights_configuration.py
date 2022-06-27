# Class for knights configuration
class KnightsConfig:

    def __init__(self, name: str, hp: int, protection: int, power: int):
        self.name = name
        self.hp = hp
        self.protection = protection
        self.power = power

    def versus(self, enemy):
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection
        if self.hp <= 0:
            self.hp = 0
        if enemy.hp <= 0:
            enemy.hp = 0


# Function that configurate knights with KnightsConfig class
def knights_configuration(knights):

    for key_name, properties in knights.items():

        # apply name
        name = properties["name"]

        # configurate health
        hp = properties["hp"]

        # apply armour
        protection = 0
        for armour in properties["armour"]:
            protection += armour["protection"]

        # apply weapon
        power = properties["power"] + properties["weapon"]["power"]

        # apply potion if exist
        skills = {"hp": hp, "protection": protection, "power": power}
        if properties["potion"] is not None:
            for key, value in skills.items():
                if key in properties["potion"]["effect"]:
                    value += properties["potion"]["effect"][key]
                    skills[key] = value

        knight = KnightsConfig(name, skills["hp"], skills["protection"], skills["power"])
        knights[key_name] = knight
    return knights
