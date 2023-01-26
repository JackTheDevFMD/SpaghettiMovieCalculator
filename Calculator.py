
# All the letters from the spaghetti can.

letters = {
    "a": 25,
    "b": 25,
    "c": 26,
    "d": 40,
    "e": 23,
    "f": 25,
    "g": 29,
    "h": 38,
    "i": 39,
    "j": 35,
    "k": 43,
    "l": 29,
    "m": 33,
    "n": 30,
    "o": 387,
    "p": 26,
    "q": 34,
    "r": 34,
    "s": 43,
    "t": 41,
    "v": 43,
    "u": 41,
    "v": 17,
    "w": 15,
    "x": 24,
    "y": 38,
    "z": 41,
}

baseLetters = 'abcdefghijklmnopqrstuvwxyz'
movie = "BeeMovie"

with open(f'{movie}.txt') as movieScript:
    script = movieScript.readlines()



class SpaghettiLettersMovies:
    def __init__(self, letterslist, baseLetters, script, movie):
        self.__movie = movie
        self.__script = script
        self.__finalCanAmount = 0
        self.__cansList = []
        self.__lettersCounter = {}
        self.__sortedLetters = []
        self.__letters = letterslist
        self.__baseLetters = list(baseLetters)

    def calculateCans(self):

        # Figure out how many cans of spaghetti's it would need to write this
        # script
        
        for eachLetter in self.__script:
            if eachLetter in self.__baseLetters:
                if eachLetter not in self.__lettersCounter:
                    self.__lettersCounter[eachLetter] = 1
                else:
                    self.__lettersCounter[eachLetter] += 1
            else:
                pass

        self.__sortedLetters = sorted(self.__lettersCounter.items())

        # Loop through each item, divide it by the amount possible in one can.
        # Append to list. 

        for eachItem in range(0, len(self.__sortedLetters)):
            self.__cansList.append((
                self.__sortedLetters[eachItem][1] /
                (self.__letters[self.__sortedLetters[eachItem][0]])
            ))
        
        # Loop through all the letters and find the highest number of cans
        # required. This will be our final answer!
        
        for eachAverages in self.__cansList:
            if eachAverages >= self.__finalCanAmount:
                self.__finalCanAmount = eachAverages

        print(f"""To write the entire movie script of {self.__movie} you would need:

{round(self.__finalCanAmount)}

Cans of Alphabet Spaghetti!
""")

spaghettis = SpaghettiLettersMovies(
    letterslist=letters,
    baseLetters=baseLetters,
    script=''.join(script),
    movie=movie
)
spaghettis.calculateCans()
