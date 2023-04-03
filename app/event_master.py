import os
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame



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
        print("In the Kingdom of Mateland, in the mid to late XI-th century,\non a sunny spring "
              "day, a huge gatekeeper, a knight,\nasks for your name before allowing entry to the "
              "tournament")
        user_name = input("Enter your name: ")
        text = "\n\nLadies and gentlemen, welcome to the knight's tournament!\nMy name is Roman " \
               "the " \
               "Apostle and I will be hosting this thrilling tournament.\nToday is a special " \
               "day as we are honored to have with us the KING himself,\nMATEthew the " \
               "PYTHONheart, whose kindness and support have helped us to organize this " \
               "tournament at the highest level!\nThank you all for joining us today, and I hope you enjoy the show!"
        time.sleep(0.000001)

        return text

    @narrative_speed(cps=1000)
    @staticmethod
    def knights_preparing():
        pass

    @narrative_speed(cps=1000)
    @staticmethod
    def knights_fight():
        pass
