class Preparation:
    def __init__(self, knight):
        self.knight = knight

    def __iter__(self):
        self.current_element = 0

    def __next__(self):

        for name_knight, value in self.knight.items():
            current_knight = {name_knight: {}}

            current_knight[name_knight] = value

            # apply armour
            current_knight[name_knight]["protection"] = 0

            for a in value["armour"]:
                current_knight[name_knight]["protection"] += a["protection"]

            # apply weapon
            current_knight[name_knight]["power"] += value["weapon"]["power"]

            # apply potion if exist
            if current_knight[name_knight]["potion"]:

                if "power" in value["potion"]["effect"]:
                    current_knight[name_knight]["power"] += \
                        value["potion"]["effect"]["power"]

                if "protection" in value["potion"]["effect"]:
                    current_knight[name_knight]["protection"] += \
                        value["potion"]["effect"]["power"]

                if "hp" in value["potion"]["effect"]:
                    current_knight[name_knight]["hp"] += \
                        value["potion"]["effect"]["hp"]

            self.knight.pop(name_knight)
            return current_knight
