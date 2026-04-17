from app.models.equipment import Weapon, Armor, Potion


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]

        # Инициализация снаряжения
        self.weapon = Weapon(config["weapon"])
        self.armor = Armor(config["armour"])
        self.potion = Potion(config.get("potion"))

        # Итоговые статы
        self.hp = 0
        self.power = 0
        self.protection = 0
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        """Применяет снаряжение и зелья к базовым статам."""
        self.hp = self.base_hp + self.potion.hp_mod
        self.power = (
            self.base_power
            + self.weapon.power
            + self.potion.power_mod
        )
        self.protection = self.armor.protection + self.potion.protection_mod

    def take_damage(self, opponent_power: int) -> None:
        """Вычисляет урон и следит, чтобы HP не упало ниже 0."""
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp = max(0, self.hp - damage)
