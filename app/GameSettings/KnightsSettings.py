import app.GameSettings.DemoKnightsSettings as Demo


class KnightsSettings:
    def __init__(self, knights_settings=None):
        if isinstance(knights_settings, dict):
            self.knights_settings = knights_settings
        else:
            self.knights_settings = \
                Demo.DemoKnightsSettings.get_demo_settings()
