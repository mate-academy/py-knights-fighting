from __future__ import annotations


from app.knights_сonfig import knights


def battle(knights_config: dict) -> dict:

    class Knight:

        def __init__(self, knight: dict) -> None:
            self.name = knight["name"]
            self.hp = knight["hp"]
            self.power = knight["power"] + knight["weapon"]["power"]
            self.protection = 0
            for armour in knight["armour"]:
                self.protection += armour["protection"]
            if knight["potion"] is not None:
                if "power" in knight["potion"]["effect"]:
                    self.power += knight["potion"]["effect"]["power"]

                if "protection" in knight["potion"]["effect"]:
                    self.protection += knight["potion"]["effect"]["protection"]

                if "hp" in knight["potion"]["effect"]:
                    self.hp += knight["potion"]["effect"]["hp"]

        @staticmethod
        def fight(first_knight: Knight, second_knight: Knight) -> None:
            first_knight.hp = max(
                0,
                first_knight.hp - (
                    second_knight.power - first_knight.protection
                )
            )
            second_knight.hp = max(
                0,
                second_knight.hp - (
                    first_knight.power - second_knight.protection
                )
            )

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    Knight.fight(lancelot, mordred)
    Knight.fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights))
