class PlayerStatus:
    def __init__(self, player: object) -> None:
        self.player = player

    def player_stats(self) -> dict:
        result_weapon = getattr(self.player, "weapon")
        result_armour = getattr(self.player, "armour")
        result_potion = getattr(self.player, "potion")
        player_attrs = {
            "name": getattr(self.player, "name"),
            "hp": getattr(self.player, "hp"),
            "power": getattr(self.player, "power"),
            "protection": getattr(self.player, "protection")
        }
        if result_potion is not None:
            player_attrs["hp"] += (
                result_potion.get("effect", {}).get("hp", 0))
            player_attrs["power"] += (
                result_potion.get("effect", {}).get("power", 0))
            player_attrs["protection"] += (
                result_potion.get("effect", {}).get("protection", 0))

        if result_armour is not None:
            player_attrs["protection"] += (
                sum(row["protection"] for row in result_armour))

        if result_weapon:
            player_attrs["power"] += result_weapon.get("power", 0)
        return player_attrs
