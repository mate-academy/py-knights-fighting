from typing import List, Dict, Any


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: List[Dict[str, int]],
                 weapon: Dict[str, Any],
                 potion: Dict[str, Any]
                 ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = 0
        self.calculate_stats()

    def calculate_stats(self) -> None:
        self.protection = sum(
            part["protection"] for part in self.armour
        )
        self.power = self.base_power + self.weapon["power"]
        if self.potion:
            self.apply_potion_effects()

    def apply_potion_effects(self) -> None:
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]
        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]
        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]


class Battle:
    @staticmethod
    def simulate_battle(
            attacker: Knight,
            defender: Knight
    ) -> None:
        damage_to_defender = max(
            0, attacker.power - defender.protection
        )
        defender.hp -= damage_to_defender

    @staticmethod
    def run_battle(
            knight1: Knight,
            knight2: Knight
    ) -> None:
        Battle.simulate_battle(knight1, knight2)
        Battle.simulate_battle(knight2, knight1)

    @staticmethod
    def get_battle_results(
            knights: List[Knight]
    ) -> Dict[str, int]:
        return {knight.name: max(knight.hp, 0) for knight in knights}


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
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def apply_effects(entity: Dict, effect: Dict) -> None:
    if "power" in effect:
        entity["power"] += effect["power"]
    if "protection" in effect:
        entity["protection"] += effect["protection"]
    if "hp" in effect:
        entity["hp"] += effect["hp"]


def prepare_entity(entity: Dict) -> None:
    entity["protection"] = sum(arm["protection"] for arm in entity["armour"])
    entity["power"] += entity["weapon"]["power"]
    if entity["potion"]:
        apply_effects(entity, entity["potion"]["effect"])


def battle(knights: Dict) -> Dict:
    # BATTLE PREPARATIONS:
    for knight in knights.values():
        prepare_entity(knight)

    # BATTLE:
    lancelot, arthur, mordred, red_knight = knights.values()

    lancelot_damage = max(0, lancelot["power"] - mordred["protection"])
    mordred_damage = max(0, mordred["power"] - lancelot["protection"])
    lancelot["hp"] -= mordred_damage
    mordred["hp"] -= lancelot_damage

    arthur_damage = max(0, arthur["power"] - red_knight["protection"])
    red_knight_damage = max(0, red_knight["power"] - arthur["protection"])
    arthur["hp"] -= red_knight_damage
    red_knight["hp"] -= arthur_damage

    # Update HPs
    lancelot["hp"] = max(lancelot["hp"], 0)
    mordred["hp"] = max(mordred["hp"], 0)
    arthur["hp"] = max(arthur["hp"], 0)
    red_knight["hp"] = max(red_knight["hp"], 0)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


def battle_main(
        config: Dict[str, Any]
) -> Dict[str, int]:
    lancelot = Knight(**config["lancelot"])
    arthur = Knight(**config["arthur"])
    mordred = Knight(**config["mordred"])
    red_knight = Knight(**config["red_knight"])

    Battle.run_battle(lancelot, mordred)
    Battle.run_battle(arthur, red_knight)

    return Battle.get_battle_results(
        [lancelot,
         arthur,
         mordred,
         red_knight]
    )


print(battle_main(KNIGHTS))
