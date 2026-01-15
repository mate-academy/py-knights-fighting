class Potion:
    def __init__(self, effects: dict = None) -> None:
        self.hp_boost = 0
        self.power_boost = 0
        self.protection_boost = 0

        if effects is not None:
            if "hp" in effects["effect"].keys():
                self.hp_boost = effects["effect"]["hp"]

            if "power" in effects["effect"].keys():
                self.power_boost = effects["effect"]["power"]

            if "protection" in effects["effect"].keys():
                self.protection_boost = effects["effect"]["protection"]
