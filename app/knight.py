class Knight:
    def __init__(self, name: str, base_hp: int, base_power: int,
                 armour: list, weapon: dict, potion: dict | None) -> None:
        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        # Ініціалізуємо поточні стати базовими значеннями
        self.hp = base_hp
        self.power = base_power
        self.protection = 0

    def prepare_stats(self) -> None:
        # 1. обов'язково: Скидаємо стати до базових перед розрахунком
        # Це робить метод безпечним для повторного виклику
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        # 2. Рахуємо захист від броні
        self.protection = sum(part["protection"] for part in self.armour)

        # 3. Додаємо силу зброї
        self.power += self.weapon["power"]

        # 4. Застосовуємо зілля (якщо є)
        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        return cls(
            name=config["name"],
            base_hp=config["hp"],
            base_power=config["power"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"]
        )
