class Battles:
    def duel(self, k1: dict, k2: dict) -> None:
        k1["hp"] -= k2["power"] - k1["protection"]
        k2["hp"] -= k1["power"] - k2["protection"]

        if k1["hp"] <= 0:
            k1["hp"] = 0

        if k2["hp"] <= 0:
            k2["hp"] = 0

    def run(self, knights: dict) -> dict:
        # 1 Lancelot vs Mordred:
        self.duel(knights["lancelot"], knights["mordred"])

        # 2 Arthur vs Red Knight:
        self.duel(knights["arthur"], knights["red_knight"])

        # Return battle results:
        return {
            knights["lancelot"]["name"]: knights["lancelot"]["hp"],
            knights["arthur"]["name"]: knights["arthur"]["hp"],
            knights["mordred"]["name"]: knights["mordred"]["hp"],
            knights["red_knight"]["name"]: knights["red_knight"]["hp"],
        }
