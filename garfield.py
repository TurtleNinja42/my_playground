import random
import time
from termcolor import colored
from simpleeval import simple_eval


class Bot:

    wait = 1

    def __init__(self):
        self.q = ''

    def _think(self, s):
        return s
    
    def _format(self, s):
        return colored(s, 'blue')

    def _say(self, s):
        time.sleep(Bot.wait)
        print(self._format(s))
        
    def run(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))


class HelloBot(Bot):

    def __init__(self):
        self.q = "Hi, what's your name?"

    def _think(self, s):
        return f"Hello, {s}! Glad to see you!"


class FeelingBot(Bot):

    def __init__(self):
        self.q = "How are you feeling today?"

    def _think(self, s):
        if ('good' in s.lower()) or ('great' in s.lower()):
            return "I'm feeling good too!"
        else:
            return 'Oh, sorry to hear that.'


class FavcolorBot(Bot):

    def __init__(self):
        self.q = "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? What a nice color! My favorite color is {random.choice(colors)}."
    

class CalcBot(Bot):

    def __init__(self):
        self.q = "Through recent upgrade I've leart how to calculate. Input some arithmetic expression to try."

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"


class Garfield:

    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []

    def add(self, bot):
        self.bots.append(bot)
        
    def run(self):
        print("This is Garfield dialog system. Feel free to talk.")
        print()

        for bot in self.bots:
            bot.run()


garfield = Garfield()

# garfield.add(HelloBot())
# garfield.add(FeelingBot())
# garfield.add(FavcolorBot())
garfield.add(CalcBot())

garfield.run()