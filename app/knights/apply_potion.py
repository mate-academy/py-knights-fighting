class Potion:

    @staticmethod
    def app_potion(potion: dict, power, hp, protection):
        stats = ["power", "hp", "protection"]
        stats_ = [power, hp, protection]
        for i in range(len(stats)):
            if stats[i] in potion["effect"]:
                stats_[i] += potion["effect"][stats[i]]

        return stats_[0], stats_[1], stats_[2]
