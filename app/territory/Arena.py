from __future__ import annotations

from app.character.Character import Character


class Arena:
    def __init__(self) -> None:
        self.participants: list[Character] = []

    def add_participant(self, participant: Character) -> None:
        self.participants.append(participant)

    def start_battle(self) -> None:
        for participant in self.participants:
            for enemy_number in range(len(self.participants)):
                if participant is not self.participants[enemy_number]:
                    participant.hit(self.participants[enemy_number])
