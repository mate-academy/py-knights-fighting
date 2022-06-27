from app.knights_list import knights


class KnightsConfig:  # Class for knights configuration

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


configured_knights = {}


def knights_configuration():

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
        if properties["potion"] is not None:
            if "power" in properties["potion"]["effect"]:
                power += properties["potion"]["effect"]["power"]

            if "protection" in properties["potion"]["effect"]:
                protection += properties["potion"]["effect"]["protection"]

            if "hp" in properties["potion"]["effect"]:
                hp += properties["potion"]["effect"]["hp"]

        knight = KnightsConfig(name, hp, protection, power)
        configured_knights[key_name] = knight


knights_configuration()
