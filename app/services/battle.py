from app.services.prepare import prepare_knight


class Battle:
    def __init__(self, knight1: str, knight2: str) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> dict:
        self.knight1.take_damage(self.knight2.power - self.knight1.protection)
        self.knight2.take_damage(self.knight1.power - self.knight2.protection)

        return {
            self.knight1.name : self.knight1.hp,
            self.knight2.name : self.knight2.hp
        }

    @staticmethod
    def battle(knights_config: dict) -> dict:
        lancelot = prepare_knight(knights_config["lancelot"])
        mordred = prepare_knight(knights_config["mordred"])
        arthur = prepare_knight(knights_config["arthur"])
        red_knight = prepare_knight(knights_config["red_knight"])

        lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        mordred["hp"] -= lancelot["power"] - mordred["protection"]

        if lancelot["hp"] <= 0:
            lancelot["hp"] = 0

        if mordred["hp"] <= 0:
            mordred["hp"] = 0

        arthur["hp"] -= red_knight["power"] - arthur["protection"]
        red_knight["hp"] -= arthur["power"] - red_knight["protection"]

        if arthur["hp"] <= 0:
            arthur["hp"] = 0

        if red_knight["hp"] <= 0:
            red_knight["hp"] = 0
        return {
            lancelot["name"]: lancelot["hp"],
            arthur["name"]: arthur["hp"],
            mordred["name"]: mordred["hp"],
            red_knight["name"]: red_knight["hp"],
        }
