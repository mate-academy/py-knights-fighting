def fight(
    first: object,
    second: object,
) -> None:
    first_damage = (
        second.power
        - first.protection
    )

    second_damage = (
        first.power
        - second.protection
    )

    first.receive_damage(first_damage)
    second.receive_damage(second_damage)
