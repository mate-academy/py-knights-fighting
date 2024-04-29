from app.players.knight import Knight


def duel(player1: Knight, player2: Knight) -> None:
    if not player1.hp or not player2.hp:
        return
    player1.hp -= player2.power - player1.protection
    player2.hp -= player1.power - player2.protection
