class Battle:
    def __init__(self, profile):
        self.profile = profile

    def armour_preparation(self):
        for stat in self.profile.values():
            stat["protection"] = 0
            for a in stat["armour"]:
                stat["protection"] += a["protection"]
        return self.profile

    def weapon_preparation(self):
        for stat in self.profile.values():
            stat["power"] += stat["weapon"]["power"]
        return self.profile

    def potion_preparation(self):
        for stat in self.profile.values():
            if stat["potion"] is not None:
                if "power" in stat["potion"]["effect"]:
                    stat["power"] += stat["potion"]["effect"]["power"]

                if "protection" in stat["potion"]["effect"]:
                    stat["protection"] +=\
                        stat["potion"]["effect"]["protection"]

                if "hp" in stat["potion"]["effect"]:
                    stat["hp"] += stat["potion"]["effect"]["hp"]
        return self.profile

    def fight(self, knight1, knight2):
        self.profile[knight1]["hp"] -=\
            self.profile[knight2]["power"] -\
            self.profile[knight1]["protection"]
        self.profile[knight2]["hp"] -=\
            self.profile[knight1]["power"] -\
            self.profile[knight2]["protection"]

        if self.profile[knight1]["hp"] <= 0:
            self.profile[knight1]["hp"] = 0

        if self.profile[knight2]["hp"] <= 0:
            self.profile[knight2]["hp"] = 0

        return {
            self.profile[knight]["name"]: self.profile[knight]["hp"]
            for knight in self.profile
        }
