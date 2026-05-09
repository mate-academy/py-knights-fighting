from app.action.battle import battle
from app.models.stats import knights_stats

result = battle(knights_stats)

print(f"Battle results: {result}")
