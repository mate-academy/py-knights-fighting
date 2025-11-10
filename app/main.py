from __future__ import annotations
from typing import Any, List, Dict, Optional

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


class Item:
    """Базовий клас для зброї, елементів обладунків та зілля."""

    def __init__(self, data: Dict[str]) -> None:
        self.name: str = data.get("name")
        # Атрибути залежать від типу предмета
        self.power: int = data.get("power")
        self.protection: int = data.get("protection")
        self.part: Optional[str] = data.get("part")  # Для обладунків
        self.effect: Optional[Dict[str, int]] = data.get("effect")  # Для зілля


class Knight:
    """Представляє Лицаря з усіма його характеристиками та поведінкою."""

    def __init__(self, data: Dict[str, Any]) -> None:
        self.name: str = data["name"]
        self.base_power: int = data["power"]
        self.hp: int = data["hp"]

        # Предмети, перетворені на об'єкти класу Item
        self.armour: List[Item] = [Item(a) for a in data.get("armour", [])]
        self.weapon: Item = Item(data["weapon"])
        self.potion: Optional[Item] = Item(data["potion"]) \
            if data["potion"] else None

        # Характеристики для битви (будуть розраховані пізніше)
        self.total_power: int = 0
        self.total_protection: int = 0

    def prepare_for_battle(self) -> None:
        """Розраховує остаточні характеристики перед боєм."""

        # 1. Базова сила + сила зброї
        self.total_power = self.base_power + self.weapon.power

        # 2. Захист від обладунків
        self.total_protection = sum(a.protection for a in self.armour)

        # 3. Застосування ефекту зілля
        if self.potion and self.potion.effect:
            effect = self.potion.effect

            self.total_power += effect.get("power", 0)
            self.total_protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)  # Зміна HP перед боєм

    def attack(self, target: Knight) -> None:
        """Лицар атакує ціль, розраховуючи шкоду."""

        # Шкода = max(0, Атакуюча сила - Захист цілі)
        damage = max(0, self.total_power - target.total_protection)
        target.hp -= damage

        # HP не може бути менше 0
        target.hp = max(0, target.hp)

    def __repr__(self) -> str:
        """Представлення об'єкта для друку."""
        return (f"Knight(Name={self.name}"
                f", HP={self.hp}"
                f", Power={self.total_power}"
                f", Prot={self.total_protection})")

    @property
    def is_alive(self) -> bool:
        """Перевіряє, чи живий лицар."""
        return self.hp > 0


def battle(knights_data: Dict[str, Any]) -> Dict[str, int]:
    # 1. 🏰 Створення об'єктів та підготовка до битви
    knights = {key: Knight(data) for key, data in knights_data.items()}

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    for knight in knights.values():
        knight.prepare_for_battle()

    # 2. 🛡️ Битва: Лицарі атакують один одного

    # Lancelot vs Mordred
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # Arthur vs Red Knight
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    # 3. 📝 Повернення результатів
    return {
        k.name: k.hp
        for k in knights.values()
    }


# Виконання
print(battle(KNIGHTS))
