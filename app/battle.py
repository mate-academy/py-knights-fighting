from app.litsar import calculate_stats


def battle(knights: dict) -> dict:
    stats = {}
    for key, knight in knights.items():
        stats[key] = calculate_stats(knight)

    stats.get("lancelot", {}).update({
        "hp": max(0, stats.get("lancelot", {}).get("hp", 0) - (
            stats.get("mordred", {}).get("power", 0)
            - stats.get("lancelot", {}).get("protection", 0)
        ))
    })

    stats.get("mordred", {}).update({
        "hp": max(0, stats.get("mordred", {}).get("hp", 0) - (
            stats.get("lancelot", {}).get("power", 0)
            - stats.get("mordred", {}).get("protection", 0)
        ))
    })

    stats.get("arthur", {}).update({
        "hp": max(0, stats.get("arthur", {}).get("hp", 0) - (
            stats.get("red_knight", {}).get("power", 0)
            - stats.get("arthur", {}).get("protection", 0)
        ))
    })

    stats.get("red_knight", {}).update({
        "hp": max(0, stats.get("red_knight", {}).get("hp", 0) - (
            stats.get("arthur", {}).get("power", 0)
            - stats.get("red_knight", {}).get("protection", 0)
        ))
    })

    return {
        stats.get("lancelot", {}).get("name", "unknown"):
            stats.get("lancelot", {}).get("hp", 0),
        stats.get("arthur", {}).get("name", "unknown"):
            stats.get("arthur", {}).get("hp", 0),
        stats.get("mordred", {}).get("name", "unknown"):
            stats.get("mordred", {}).get("hp", 0),
        stats.get("red_knight", {}).get("name", "unknown"):
            stats.get("red_knight", {}).get("hp", 0),
    }
