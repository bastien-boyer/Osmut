
from enum import Enum

class Color(Enum):
    RED = 1
    YELLOW = 2
    BLUE = 3
    GREEN = 4


ALPHA_REF = "./filesReference/asciiArtReference.txt"

class AsciiArt():
    def __init__(self) -> None:
        self.alpha_map = self.populate_alpha_map()
        self.width = 20
        self.height = 11
        self.letters = self.getAsciiLetters()
    
    def populate_alpha_map(self):
        alpha_map = {}
        for i, c in enumerate(range(ord('A'), ord('Z') + 1)):
            alpha_map[chr(c)] = i
        alpha_map['_'] = 26
        return alpha_map

    def getAsciiLetters(self):
        letters = []
        alphaRef = open(ALPHA_REF)
        for i in alphaRef:
            row = i
            letters.append(row)
        return letters

    def painting(self, text, colors):
        """
        Each letter has a height and a width
        Each iteration print an entire line 
        """

        tmp = ""
        start, end = 0, 0
        for h in range(self.height):
            c = 0
            for char in text:
                if self.alpha_map.get(char) is None:
                    start = self.alpha_map.get('_') * self.width
                else:
                    start = self.alpha_map.get(char) * self.width
                end = start + self.width
                tmp += self.create_art(self.letters, start, end, h, colors[c] if colors else Color.GREEN)
                c += 1
            print(tmp)
            tmp = ""


    def create_art(self, letter, start, end, height, color):
        tmp = ""
        for i in range(start, end):
            if color == Color.RED:
                tmp += self.goodLetterInRightEmplacement(letter[height][i])
            elif color == Color.YELLOW:
                tmp += self.goodLetterButWrongEmplacement(letter[height][i])
            elif color == Color.BLUE:
                tmp += self.badLetter(letter[height][i])
            else :
                tmp += self.print_endGame(letter[height][i])
        return tmp


    def print_endGame(self, letter):
        # GREEN
        return "\033[32m" + letter + "\033[0m"

    def badLetter(self, letter):
        # Blue
        return "\033[34m" + letter + "\033[0m"

    def goodLetterButWrongEmplacement(self, letter):
        # Yellow
        return "\033[33m" + letter + "\033[0m"

    def goodLetterInRightEmplacement(self, letter):
        # RED
        return "\033[31m" + letter + "\033[0m"

if __name__ == "__main__":
    """"""