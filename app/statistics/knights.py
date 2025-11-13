class Tournament:
    lancelot: dict
    arthur: dict
    mordred: dict
    red_knight: dict
    list_knights: list["Tournament"] = []
    def __init__(self, data: dict, protection: int = 0) -> None:
        self.protection = protection
        for key, value in data.items():
            setattr(self, key, value)
            Tournament.list_knights.append(getattr(self, key))

    @staticmethod
    def configurations(stat):
        stat["protection"] = 0
        for a in stat["armour"]:
            stat["protection"] += a["protection"]

        # apply weapon
        stat["power"] += stat["weapon"]["power"]

        # apply potion if exist
        if stat["potion"] is not None:
            if "power" in stat["potion"]["effect"]:
                stat["power"] += stat["potion"]["effect"]["power"]

            if "protection" in stat["potion"]["effect"]:
                stat["protection"] += stat["potion"]["effect"]["protection"]

            if "hp" in stat["potion"]["effect"]:
                stat["hp"] += stat["potion"]["effect"]["hp"]

    @staticmethod
    def battle(knight1, knight2):
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]
        if knight1["hp"] <= 0:
            knight1["hp"] = 0

        if knight2["hp"] <= 0:
            knight2["hp"] = 0
