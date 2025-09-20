def split_dict1(data: dict) -> list:
    pairs = []
    items = list(data.items())
    length_list = len(items)
    ilosc_par = int(length_list // 2)
    first_knights = items[:ilosc_par]
    second_knights = items[ilosc_par:]
    for ind in range(ilosc_par):
        pair = {}
        knight = list(first_knights[ind])
        enemy = list(second_knights[ind])
        pair.update({knight[0]: knight[1]})
        pair.update({enemy[0]: enemy[1]})
        pairs.append(pair)
    return pairs
