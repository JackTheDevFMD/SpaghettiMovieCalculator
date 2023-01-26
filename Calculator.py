
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
movies = {
    "The Bee Movie": "BeeMovie",
    "The IrishMan": "irish",
    "John Wick (2014)": "JohnWick",
    "The wolf of Wall Street": "wolf",
    "The batman": "batman",
    "Avatar (2009)": "avatar",
    "Lord of the Rings : The Return of the King": "lordoftherings",
    "The Lord of the Rings : The Two Towers": "lordoftherings2",
    "The Lord of the Rings : The Return of the King": "lordoftherings3"
}

movieChosing = True


while movieChosing:

    print("Please chose which movie you want to see data on:")
    
    for eachItem in movies:
        print(eachItem)
        
    userMovie = input("")

    if userMovie == "":
        pass
    else:
        try:
            movie = movies[userMovie]
            movieChosing = False
        except:
            print("Uh oh")




with open(f'scripts/{movie}.txt', encoding="utf8") as movieScript:
    script = movieScript.readlines()


class SpaghettiLettersMovies:
    def __init__(self, letterslist, baseLetters, script, movie):
        self.__movie = movie
        self.__script = script.lower()
        self.__cansList = []
        self.__lettersCounter = {}
        self.__sortedLetters = []
        self.__letters = letterslist
        self.__baseLetters = list(baseLetters)
        self.__finalCanAmount = 0
        self.__highestLetters = ('a', 0)
        self.__lowestLetters = ('a', 10000)

    def calculateCans(self):

        # Figure out how many cans of spaghetti's it would need to write this
        # script
        
        for eachLetter in self.__script:
            if eachLetter in self.__baseLetters:
                if eachLetter not in self.__lettersCounter:
                    self.__lettersCounter[eachLetter] = 1
                else:
                    self.__lettersCounter[eachLetter] += 1

        # Sorts list into alphabetical order according to the items in
        # self.__lettersCounter
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

        # Data about the movie

        print(f"In the movie {self.__movie} there was:")
        for eachLetterCounter in self.__sortedLetters:
            if eachLetterCounter[1] >= self.__highestLetters[1]:
                self.__highestLetters = eachLetterCounter
                
            if eachLetterCounter[1] < self.__lowestLetters[1]:
                self.__lowestLetters = eachLetterCounter
                
            print(f"{eachLetterCounter[0]} : {eachLetterCounter[1]}")

        print(f"""\n\nThe most letters in the script is: \n
{self.__highestLetters}\n\n""")
        print(f"""The least amount of letters in the script is: \n
{self.__lowestLetters}\n\n""")
        

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
