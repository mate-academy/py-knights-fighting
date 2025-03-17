class BATTLE:
    def apply_armour(self, knight: dict) -> None:
        """Обчислює загальний рівень захисту лицаря, сумуючи всю його броню."""
        knight["protection"] = sum(piece["protection"]
                                   for piece in knight["armour"])

    def apply_weapon(self, knight: dict) -> None:
        knight["power"] += knight["weapon"]["power"]

    def apply_potion(self, knight: dict) -> None:
        """Застосовує ефект зілля до параметрів лицаря."""
        if knight["potion"]:
            effect = knight["potion"]["effect"]
            knight["power"] += effect.get("power", 0)
            knight["hp"] += effect.get("hp", 0)
            knight["protection"] += effect.get("protection", 0)

    def prepare_knight(self, knight: dict) -> None:
        """Підготовка лицаря: броня, зброя, зілля."""
        self.apply_armour(knight)
        self.apply_weapon(knight)
        self.apply_potion(knight)

    def battle(self, knights_config: dict) -> dict:
        """Основна логіка битви між лицарями."""

        # Підготовка кожного лицаря
        for knight in knights_config.values():
            self.prepare_knight(knight)

        # Отримуємо параметри
        lancelot = knights_config["lancelot"]
        mordred = knights_config["mordred"]
        arthur = knights_config["arthur"]
        red_knight = knights_config["red_knight"]

        # Битва: Lancelot vs Mordred
        lancelot["hp"] -= max(0, mordred["power"] - lancelot["protection"])
        mordred["hp"] -= max(0, lancelot["power"] - mordred["protection"])

        # Битва: Arthur vs Red Knight
        arthur["hp"] -= max(0, red_knight["power"] - arthur["protection"])
        red_knight["hp"] -= max(0, arthur["power"] - red_knight["protection"])

        # Уникнення від'ємного hp
        for knight in [lancelot, mordred, arthur, red_knight]:
            knight["hp"] = max(0, knight["hp"])

        return {
            lancelot["name"]: lancelot["hp"],
            arthur["name"]: arthur["hp"],
            mordred["name"]: mordred["hp"],
            red_knight["name"]: red_knight["hp"],
        }
