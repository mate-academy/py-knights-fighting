def appoint_opponent(participants_knights: dict) -> None:
    for nickname in participants_knights:
        knight = participants_knights[nickname]
        if knight.name == "Lancelot":
            knight.opponents(participants_knights, "Lancelot", "Mordred")
        if knight.name == "Arthur":
            knight.opponents(participants_knights, "Arthur", "Red Knight")
