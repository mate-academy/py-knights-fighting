# Клас, що виводить лицаря та його характеристики
class Knight:
    def __init__(self, knight_data):
        # Основниі характеристики лицаря
        self.name = knight_data["name"]
        self.base_hp = knight_data["hp"]
        self.base_power = knight_data["power"]
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]

        # Розрахункові характеристики
        self.protection = 0
        self.hp = self.base_hp
        self.power = self.base_power

        # Застосування екіпірування
        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self):
        """Розрахувати захист з броні"""
        for item in self.armour:
            self.protection += item["protection"]

    def _apply_weapon(self):
        """Додати силу зброї до базової сили"""
        self.power += self.weapon["power"]

    def _apply_potion(self):
        """Застосувати ефекти зілля до характеристик"""
        if self.potion is None:
            return

        effects = self.potion["effect"]
        # Оновлення характеристик згідно з ефектами зілля
        for stat, value in effects.items():
            if hasattr(self, stat):
                current_value = getattr(self, stat)
                setattr(self, stat, current_value + value)

    def take_damage(self, damage):
        """Застосувати пошкодження до здоров'я лицаря"""
        self.hp = max(0, self.hp - damage)