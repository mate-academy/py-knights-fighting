def create_battle_pairs(data: dict) -> list:
    pairs = []
    items = list(data.items())
    length_list = len(items)
    pair_numbers = int(length_list // 2)
    first_knights = items[:pair_numbers]
    second_knights = items[pair_numbers:]
    for ind in range(pair_numbers):
        pair = {}
        knight = list(first_knights[ind])
        enemy = list(second_knights[ind])
        pair.update({knight[0]: knight[1]})
        pair.update({enemy[0]: enemy[1]})
        pairs.append(pair)
    return pairs
