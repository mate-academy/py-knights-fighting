from __future__ import annotations


class Armor:
    def __init__(
            self,
            part: str,
            protection: int
    ) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(
            self,
            name: str,
            power: int
    ) -> None:
        self.name = name
        self.power = power

    @staticmethod
    def initialize(
            weapon: dict
    ) -> Weapon:
        return Weapon(weapon["name"], weapon["power"])


class Potion:
    def __init__(
            self,
            name: str,
            effect: Effect
    ) -> None:
        self.name = name
        self.effect = effect

    @staticmethod
    def check_effect(effect_dict: dict) -> Effect | bool:
        result = Effect.find_effect(Effect.make_key(effect_dict))
        if result:
            return result
        return Effect(
            health_points=effect_dict.get("hp") or 0,
            power=effect_dict.get("power") or 0,
            protection=effect_dict.get("protection") or 0
        )

    @staticmethod
    def initialize(
            potion: dict | list[dict]
    ) -> Potion | list[Potion]:
        if isinstance(potion, dict):
            return [
                Potion(
                    name=potion["name"],
                    effect=Potion.check_effect(potion["effect"])
                )
            ]
        elif isinstance(potion, list):
            return [
                Potion(
                    name=elem["name"],
                    effect=Potion.check_effect(elem["effect"]))
                for elem in potion
            ]
        elif potion is None:
            return []


class Effect:
    effects = []

    def __init__(
            self,
            health_points: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.health_points = health_points
        self.power = power
        self.protection = protection
        self.key = str(health_points) + str(power) + str(protection)
        self.effects.append(self)

    @staticmethod
    def make_key(
            effect_dict: dict[str, int]
    ) -> str:
        hp = "0"
        power = "0"
        protection = "0"
        if effect_dict.get("hp"):
            hp = str(effect_dict.get("hp"))
        if effect_dict.get("power"):
            power = str(effect_dict.get("power"))
        if effect_dict.get("protection"):
            protection = str(effect_dict.get("protection"))
        return hp + power + protection

    @classmethod
    def find_effect(
            cls,
            key: str
    ) -> Effect | False:
        if cls.effects:
            for effect in cls.effects:
                if effect.key == key:
                    return effect
        return False
