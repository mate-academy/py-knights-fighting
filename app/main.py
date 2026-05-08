KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }


class Knight:
    def __init__(self, name):
        self.name = name

    def weapon(self, name: str, power: int):
        self.power = power
        self.name = name

    def battle(knightsConfig):
        lancelot = knightsConfig["lancelot"]
        lancelot["protection"] = sum(a["protection"] for a in lancelot["armour"])
        lancelot["power"] += lancelot["weapon"]["power"]

        if lancelot["potion"] is not None:
            if "power" in lancelot["potion"]["effect"]:
                lancelot["power"] += lancelot["potion"]["effect"]["power"]
            if "protection" in lancelot["potion"]["effect"]:
                lancelot["protection"] += lancelot["potion"]["effect"]["protection"]
            if "hp" in lancelot["potion"]["effect"]:
                lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

        arthur = knightsConfig["arthur"]
        arthur["protection"] = sum(a["protection"] for a in arthur["armour"])
        arthur["power"] += arthur["weapon"]["power"]

        if arthur["potion"] is not None:
            if "power" in arthur["potion"]["effect"]:
                arthur["power"] += arthur["potion"]["effect"]["power"]
            if "protection" in arthur["potion"]["effect"]:
                arthur["protection"] += arthur["potion"]["effect"]["protection"]
            if "hp" in arthur["potion"]["effect"]:
                arthur["hp"] += arthur["potion"]["effect"]["hp"]

        mordred = knightsConfig["mordred"]
        mordred["protection"] = sum(a["protection"] for a in mordred["armour"])
        mordred["power"] += mordred["weapon"]["power"]

        if mordred["potion"] is not None:
            if "power" in mordred["potion"]["effect"]:
                mordred["power"] += mordred["potion"]["effect"]["power"]
            if "protection" in mordred["potion"]["effect"]:
                mordred["protection"] += mordred["potion"]["effect"]["protection"]
            if "hp" in mordred["potion"]["effect"]:
                mordred["hp"] += mordred["potion"]["effect"]["hp"]

        red_knight = knightsConfig["red_knight"]
        red_knight["protection"] = sum(a["protection"] for a in red_knight["armour"])
        red_knight["power"] += red_knight["weapon"]["power"]

        if red_knight["potion"] is not None:
            if "power" in red_knight["potion"]["effect"]:
                red_knight["power"] += red_knight["potion"]["effect"]["power"]
            if "protection" in red_knight["potion"]["effect"]:
                red_knight["protection"] += red_knight["potion"]["effect"]["protection"]
            if "hp" in red_knight["potion"]["effect"]:
                red_knight["hp"] += red_knight["potion"]["effect"]["hp"]

        lancelot["hp"] -= max(0, mordred["power"] - lancelot["protection"])
        mordred["hp"] -= max(0, lancelot["power"] - mordred["protection"])

        lancelot["hp"] = max(0, lancelot["hp"])
        mordred["hp"] = max(0, mordred["hp"])

        arthur["hp"] -= max(0, red_knight["power"] - arthur["protection"])
        red_knight["hp"] -= max(0, arthur["power"] - red_knight["protection"])

        arthur["hp"] = max(0, arthur["hp"])
        red_knight["hp"] = max(0, red_knight["hp"])

        return {
            lancelot["name"]: lancelot["hp"],
            arthur["name"]: arthur["hp"],
            mordred["name"]: mordred["hp"],
            red_knight["name"]: red_knight["hp"],
        }

    def prepare_knight(knight):
        protection = sum(item["protection"] for item in knight["armour"])
        power = knight["power"] + knight["weapon"]["power"]
        hp = knight["hp"]
        potion = knight["potion"]
        if potion:
            effect = potion["effect"]
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)
            hp += effect.get("hp", 0)

        return {"hp": hp, "power": power, "protection": protection}
