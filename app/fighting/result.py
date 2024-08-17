def check_fight_result(knights: list) -> dict:

    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0

            print(f"{knight.name} was defeated!")

    return {knight.name: knight.hp for knight in knights}
