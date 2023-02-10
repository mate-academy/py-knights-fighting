from app.main_app_units.knights import Knight


class Arena:

    fighting_result = {}

    @classmethod
    def fight_in_arena(
            cls,
            participants: str,
            instances: dict[Knight]
    ) -> None:
        participant_a, participant_b = participants.split("_VS_")

        cls.fighting_result[
            participant_a.title().replace("h", "")
        ] = (instances[participant_a].hp
             - instances[participant_b].power)

        cls.fighting_result[
            participant_b.title().replace("_", " ")
        ] = (instances[participant_b].hp
             - instances[participant_a].power)

    @classmethod
    def death_check(cls) -> None:
        for name, hp in cls.fighting_result.items():
            if hp <= 0:
                cls.fighting_result[name] = 0
