class Knight:
    def __init__(self, name: str, base_hp: int, base_power: int,
                 armour: list, weapon: dict, potion: dict | None) -> None:
        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        # Фінальні стати (поки що 0 або базові)
        self.hp = base_hp
        self.power = base_power
        self.protection = 0

    def prepare_stats(self) -> None:
        # 1. Рахуємо захист від броні
        self.protection = sum(part["protection"] for part in self.armour)

        # 2. Додаємо силу зброї
        self.power += self.weapon["power"]

        # 3. Застосовуємо зілля (якщо є)
        if self.potion:
            effect = self.potion["effect"]
            # dict.get(key, 0) повертає 0, якщо ключа немає
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        """Зменшує HP лицаря. HP не може бути менше 0."""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        """Створює лицаря зі словника конфігурації."""
        return cls(
            name=config["name"],
            base_hp=config["hp"],
            base_power=config["power"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )
