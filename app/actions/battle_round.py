def battle_round(knights: dict) -> dict:

    knights["Lancelot"].hp -= (knights["Mordred"].power
                               - knights["Lancelot"].protection)
    knights["Mordred"].hp -= (knights["Lancelot"].power
                              - knights["Mordred"].protection)
    knights["Artur"].hp -= (knights["Red Knight"].power
                            - knights["Artur"].protection)
    knights["Red Knight"].hp -= (knights["Artur"].power
                                 - knights["Red Knight"].protection)

    return knights
