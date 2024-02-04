def versus_result(stats: dict) -> dict:
    return {
        "Lancelot": stats["lancelot"]["hp"],
        "Arthur": stats["arthur"]["hp"],
        "Mordred": stats["mordred"]["hp"],
        "Red Knight": stats["red_knight"]["hp"],
    }
