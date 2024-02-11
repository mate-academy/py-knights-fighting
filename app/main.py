from app.battle_players.battle_player import Battle
from app.player.player import Player
from app.status_player.player_status import PlayerStatus


def battle(knightsconfig: dict) -> dict:
    players = []
    for key, vel in knightsconfig.items():
        key = Player(vel)
        players.append(key)
    players_status = [PlayerStatus(player) for player in players]

    result = Battle(players_status[0].player_stats(),
                    players_status[2].player_stats(),
                    players_status[1].player_stats(),
                    players_status[3].player_stats())
    return result.battls()
