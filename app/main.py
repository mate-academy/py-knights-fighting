from app.knights.arthur import Arthur
from app.knights.lancelot import Lancelot
from app.knights.mordred import MordRed
from app.knights.red_knight import RedKnight
from app.Battle.battle import Battle
from app.status.lancelot_stats import LancelotStatus
from app.status.mordred_stats import MordredStatus
from app.status.arthur_stats import ArthurStatus
from app.status.red_knight_stats import RedKnightStatus


def battle(knightsconfig: dict) -> dict:
    lancelot = Lancelot(knightsconfig.get("lancelot"))
    arthur = Arthur(knightsconfig.get("arthur"))
    mordred = MordRed(knightsconfig.get("mordred"))
    red_knight = RedKnight(knightsconfig.get("red_knight"))
    result = Battle(LancelotStatus(lancelot), MordredStatus(mordred),
                    ArthurStatus(arthur), RedKnightStatus(red_knight))
    return result.battls()
