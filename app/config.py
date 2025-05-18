from app.knights import Knights

def get_knights():
    return {
        "Lancelot": Knights("Lancelot", 75, 100, 0),
        "Arthur": Knights("Arthur", 100, 75, 45),
        "Mordred": Knights("Mordred", 105, 85, 35),
        "Red Knight": Knights("Red Knight", 90, 80, 25),
    }