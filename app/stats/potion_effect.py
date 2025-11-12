def potion_effect(name: dict) -> None:
    if name['potion'] is not None:
        if 'power' in name['potion']['effect']:
            name['power'] += name['potion']['effect']['power']

        if 'protection' in name['potion']['effect']:
            name['protection'] += name['potion']['effect']['protection']

        if 'hp' in name['potion']['effect']:
            name['hp'] += name['potion']['effect']['hp']
