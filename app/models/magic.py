import time
from dataclasses import dataclass


@dataclass
class Magic:
    name: str
    base_power: int

    def get_power(self) -> int:
        """
        Обчислює магічну силу для Ланселота в залежності від поточного часу.

        Часові діапазони:
        - З 12:00 по 17:59: +15 до сили.
        - З 18:00 по 23:59: 0 до сили.
        - З 00:00 по 05:59: -10 до сили.
        - З 06:00 по 11:59: 0 до сили.

        Повертає значення магічної сили.
        """
        current_hour = time.localtime().tm_hour

        if 12 <= current_hour < 18:
            return self.base_power + 15
        elif 18 <= current_hour < 24:
            return self.base_power
        elif 0 <= current_hour < 6:
            return self.base_power - 10
        else:
            return self.base_power
