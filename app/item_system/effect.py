from __future__ import annotations

from adapters.effect_config import EffectConfig
from utils.formatting import number_to_string


class Effect:
    """
    Represents effect, that can increase or decrease certain stats

    Properties:
        power (int): buff/debuff to attack power
        protection (int): buff/debuff to protection
        hp (int): buff/debuff to health points
    """

    def __init__(self, effect_data: EffectConfig) -> None:
        self._power = effect_data.power
        self._protection = effect_data.protection
        self._hp = effect_data.hp

        self._total_bonus = self.hp + self.protection + self.power

    def __str__(self) -> str:
        stats: list[str] = []
        if self.hp != 0:
            stats.append(f"HP: {number_to_string(self.hp)}")
        if self.power != 0:
            stats.append(f"Power: {number_to_string(self.power)}")
        if self.protection != 0:
            stats.append(f"Protection: {number_to_string(self.protection)}")
        if stats:
            join_stats = ", ".join(stats)
            return f"{{{join_stats}}}"

        return "No apparent effect"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Effect):
            return NotImplemented

        return (
            self.hp == other.hp
            and self.power == other.power
            and self.protection == other.protection
        )

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Effect):
            return NotImplemented

        return (
            self.hp != other._hp
            and self.power != other.power
            and self.protection != other.protection
        )

    def __lt__(self, other: Effect) -> bool:
        return self.total_bonus < other.total_bonus

    def __gt__(self, other: Effect) -> bool:
        return self.total_bonus > other.total_bonus

    @property
    def power(self) -> int:
        return self._power

    @property
    def protection(self) -> int:
        return self._protection

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def total_bonus(self) -> int:
        return self._total_bonus
