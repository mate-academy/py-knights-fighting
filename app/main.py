from app.knight import Knight

def battle(knights_config):
    # 1. Criar as instâncias dos cavaleiros usando a classe
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    # 2. Executar as batalhas conforme o enunciado
    # Batalha 1: Lancelot vs Mordred
    lancelot.receive_damage(mordred.power)
    mordred.receive_damage(lancelot.power)

    # Batalha 2: Arthur vs Red Knight
    arthur.receive_damage(red_knight.power)
    red_knight.receive_damage(arthur.power)

    # 3. Retornar os HPs finais em um dicionário
    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }
