import os
import time


os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


event_counter = 0


class Event:

    def narrative_speed(cps):
        def decorator(func):
            def wrapper(*args, **kwargs):
                text = str(func(*args, **kwargs))
                for char in text:

                    print(char, end='', flush=True)
                    time.sleep(1 / cps)
            return wrapper
        return decorator

    @staticmethod
    def ambience():
        pygame.init()
        pygame.mixer.music.load('CR_TourneyBattle01UniWalk.mp3')
        pygame.mixer.music.play()

    @narrative_speed(cps=1000)
    @staticmethod
    def event_start():
        print("In the Kingdom of Mateland, in the mid to late XI-th century")
        with open('event_start.txt', 'r') as file:
            text = file.read()
        return text
    @narrative_speed(cps=1000)
    @staticmethod
    def event_fight(knight_1, knight_2):
        if knight_1.hp > knight_2.hp:
            winner = knight_1.name
            loser = knight_2.name
        else:
            winner = knight_2.name
            loser = knight_1.name

        global event_counter
        if event_counter == 0:
            event_path = 'event_fight_1.txt'
        else:
            event_path = 'event_fight_2.txt'
        with open(event_path, 'r') as file:
            text = file.read().format(
                knight_1=knight_1.name,
                knight_1_hp=knight_1.hp,
                knight_1_weapon=knight_1.weapon["name"],
                knight_2=knight_2.name,
                knight_2_weapon=knight_2.weapon["name"],
                knight_2_hp=knight_2.hp,
                winner=winner,
                loser=loser)

        event_counter += 1
        return text


    @narrative_speed(cps=1000)
    @staticmethod
    def event_result(result):

        items = result.items()
        result = [[k, v] for k, v in items]
        result.sort(key=lambda x: x[1], reverse=True)

        text = (
            "Based on the results of two battles, our judges have awarded the following number of "
            f"points to our participants:\n\n{'*' * 10}\n"
            f"{result[0][0]}: {result[0][1]}\n"
            f"{result[1][0]}: {result[1][1]}\n"
            f"{result[2][0]}: {result[2][1]}\n"
            f"{result[3][0]}: {result[3][1]}\n{'*' * 10}\n\n"
            f"Ladies and gentlemen, it is my honor to declare the winner of the tournament, Sir {result[0][0]}! "
            f"As the champion, Sir {result[0][0]} has the privilege of challenging anyone in the audience "
            "to a duel. Who among you dares to face this valiant knight?")

        return text


#
# with open('text.txt', 'r') as file:
#     X = file.read().format(knight_1=knight_1)
# #
# #
# #
#        with open('test.txt', 'r') as file:
#             text = file.read()
