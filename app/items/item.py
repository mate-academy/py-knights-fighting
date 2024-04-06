from __future__ import annotations
from abc import ABC, abstractmethod

from app.players.player import Player


class BaseItem(ABC):
    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    @abstractmethod
    def create_from_dict(cls, item: dict | None) -> BaseItem | None:
        """
        Create instance by using given dictionary.

        Args:
            item (dict): Dictionary with given attributes.
        """

    @abstractmethod
    def use(self, player: Player) -> None:
        """
        Change player attributes depending on item attributes.

        Args:
            player (Player): Player instance.
        """

    def unuse(self, player: Player) -> None:
        """
        Restore player attributes depending on item attributes.
        Potion cannot be unused.

        Args:
            player (Player): Player instance.
        """
