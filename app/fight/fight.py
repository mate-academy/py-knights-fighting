from app.initializate.knight import Knight


def show_ready_fighters(fighters: list[Knight]) -> str:
    result = [obj.show_fight_ready_knight() for obj in fighters]
    # Объединяем их в одну строку, разделяя переносами строк
    return "\n".join(result)


def get_full_info(fighters: list[Knight]) -> str:
    result = [obj.show_full_info() for obj in fighters]
    # Объединяем их в одну строку, разделяя переносами строк
    return "\n".join(result)


def fight(fighters: list[Knight]) -> None:
    result = {}
    result["fight 1"] = fighters[0].attack(fighters[2])
    result["fight 2"] = fighters[1].attack(fighters[3])
    print(result)
