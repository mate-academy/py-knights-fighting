class Battle:

    def __init__(self, l_status: object, m_status: object,
                 a_status: object, r_status: object) -> None:
        self.lancelot_status = l_status.lancelot_stats()
        self.mordred_status = m_status.mordred_stats()
        self.arthur_status = a_status.arthur_stats()
        self.red_knight_status = r_status.red_knight_stats()

    def battls(self) -> dict:
        self.lancelot_status["hp"] \
            -= (self.mordred_status["power"]
                - self.lancelot_status["protection"])
        self.mordred_status["hp"] \
            -= (self.lancelot_status["power"]
                - self.mordred_status["protection"])
        self.arthur_status["hp"] \
            -= (self.red_knight_status["power"]
                - self.arthur_status["protection"])
        self.red_knight_status["hp"] \
            -= (self.arthur_status["power"]
                - self.red_knight_status["protection"])

        if self.lancelot_status["hp"] <= 0:
            self.lancelot_status["hp"] = 0

        if self.mordred_status["hp"] <= 0:
            self.mordred_status["hp"] = 0

        if self.arthur_status["hp"] <= 0:
            self.arthur_status["hp"] = 0

        if self.red_knight_status["hp"] <= 0:
            self.red_knight_status["hp"] = 0

        return {f"""{self.lancelot_status.get("name")}""":
                self.lancelot_status.get("hp"),
                f"""{self.arthur_status.get("name")}""":
                self.arthur_status.get("hp"),
                f"""{self.mordred_status.get("name")}""":
                self.mordred_status.get("hp"),
                f"""{self.red_knight_status.get("name")}""":
                self.red_knight_status.get("hp")}
