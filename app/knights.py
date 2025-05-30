from typing import Dict, Any, List, Optional


class Knight:
    """Клас, що представляє лицаря та його характеристики."""

    def __init__(self, knight_data: Dict[str, Any]) -> None:
        """Ініціалізація лицаря з базовими характеристиками.

        Args:
            knight_data: Словник з даними про лицаря
        """
        self.name: str = knight_data["name"]
        self.base_hp: int = knight_data["hp"]
        self.base_power: int = knight_data["power"]
        self.armour: List[Dict[str, Any]] = knight_data["armour"]
        self.weapon: Dict[str, Any] = knight_data["weapon"]
        self.potion: Optional[Dict[str, Any]] = knight_data["potion"]

        self.protection: int = 0
        self.hp: int = self.base_hp
        self.power: int = self.base_power

        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        """Розрахувати захист з броні."""
        for item in self.armour:
            self.protection += item["protection"]

    def _apply_weapon(self) -> None:
        """Додати силу зброї до базової сили."""
        self.power += self.weapon["power"]

    def _apply_potion(self) -> None:
        """Застосувати ефекти зілля до характеристик."""
        if self.potion is None:
            return

        effects = self.potion["effect"]
        for stat, value in effects.items():
            if hasattr(self, stat):
                current_value = getattr(self, stat)
                setattr(self, stat, current_value + value)

    def take_damage(self, damage: int) -> None:
        """Застосувати пошкодження до здоров'я лицаря.

        Args:
            damage: Кількість пошкоджень
        """
        self.hp = max(0, self.hp - damage)
