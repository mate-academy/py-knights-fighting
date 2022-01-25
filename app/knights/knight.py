"""
This module contains class Knight, which used by main.py module
to create instances of knights choosed for competition. Class
takes two arguments - name of knight and config file with
necessary data. Instance methods make calculations, based on the config file,
and then return final version of characteristics,
needed for "fight" calculation to choose a winner.
"""


class Knight:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.knight = self.config[self.name]

    def get_hp(self):
        if self.knight["potion"] is not None:
            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]

        return self.knight["hp"]

    def get_power(self):
        self.knight["power"] += self.knight["weapon"]["power"]
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] += \
                    self.knight["potion"]["effect"]["power"]

        return self.knight["power"]

    def get_protection(self):
        self.knight["protection"] = 0
        for armour in self.knight["armour"]:
            self.knight["protection"] += armour["protection"]
        if self.knight["potion"] is not None:
            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] += \
                    self.knight["potion"]["effect"]["protection"]

        return self.knight["protection"]
