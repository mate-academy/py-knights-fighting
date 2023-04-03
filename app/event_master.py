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

    @narrative_speed(cps=1000)
    def event_start():
        pygame.init()
        pygame.mixer.music.load('CR_TourneyBattle01UniWalk.mp3')
        pygame.mixer.music.play()
        text = "Ladies and gentlemen, welcome to the grandest knight tournament in the entire " \
               "kingdom!\n" \
               "Here, the most powerful and brave knights will come together to determine who will\n" \
               "become the true hero!"
        time.sleep(0.0000000001)

        # "\nDear guests, if you believe that you have the spirit of a " \
        # "true knight,\nyou can join our fighters! \nChoose your equipment and head to the arena!"
        return text

    # scenario = input("\nWhat will you choose?:                                                   ")


event = Event