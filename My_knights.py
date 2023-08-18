class Knight:
    def __init__(self, persons: dict) -> None:
        self.persons = persons

    def preparing(self: dict) -> dict:
        result_of_preparing = {}
        for person, values in self.items():
            protection = values["protection"] = 0
            power = values["power"]
            hp = values["hp"]
            for value in values["armour"]:
                protection += value["protection"]
            power += values["weapon"]["power"]
            if values["potion"] is not None:
                if "power" in values["potion"]["effect"]:
                    power += values["potion"]["effect"]["power"]

                if "protection" in values["potion"]["effect"]:
                    protection += \
                        values["potion"]["effect"]["protection"]

                if "hp" in values["potion"]["effect"]:
                    hp += \
                        values["potion"]["effect"]["hp"]
            result_of_preparing.update({
                person: {"hp": hp,
                         "power": power,
                         "protection": protection}})
        return result_of_preparing
