from .armour_part import ArmourPart


class Armour:
    def __init__(self, armour_cfg: dict) -> None:
        self._armour_parts = []
        for armour in armour_cfg:
            self._armour_parts.append(
                ArmourPart(armour["part"], armour["protection"])
            )
        self._current_index = 0

    def __iter__(self) -> "Armour":
        return self

    def __next__(self) -> ArmourPart:
        if self._current_index < len(self._armour_parts):
            armour_part = self._armour_parts[self._current_index]
            self._current_index += 1
            return armour_part

        raise StopIteration
