from app.battle_players.battle_player import Battle
from app.player.player import Player
from app.status_player.player_status import PlayerStatus


def battle(knightsconfig: dict) -> dict:
    players = [Player(participant) for participant in knightsconfig.values()]
    players_status = [PlayerStatus(player).player_stats()
                      for player in players]
    result = Battle(players_status)
    return result.battls()
