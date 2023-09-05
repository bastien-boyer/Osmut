import sys
from scripts import asciiArt


class Game:
    def __init__(self, mysteryWord, availableList) -> None:
        self.mysteryWord = mysteryWord
        self.availableWordList = availableList
        self.originNumberOccurence = self.getDicNumberOfOccurence(mysteryWord)
        self.live = 0
        self.colors = []
        self.ascii = asciiArt.AsciiArt()
        self.wordIndice = self.createWordIndice()

    def createWordIndice(self):
        tmp = ""
        for i, letter in enumerate(self.mysteryWord):
            if i == 0:
                tmp += self.mysteryWord[i]
            else:
                tmp += "_"
        return tmp

    def checkRules(self, str):
        if str[0] != self.mysteryWord[0]:
            raise Exception(
                f"Le mot doit obligatoirement commencer par la lettre [{self.mysteryWord[0].capitalize()}]"
            )
        if len(str) != len(self.mysteryWord):
            raise Exception(
                f"Le mot doit obligatoirement comporter [{len(self.mysteryWord)}] lettres"
            )
        if str not in self.availableWordList:
            raise Exception(f"Le mot '{str}' n'est pas dans le dictionnaire")

    def getDicNumberOfOccurence(self, str):
        dictionnary = {}
        for letter in str:
            if dictionnary.get(letter) != None:
                dictionnary[letter] += 1
            else:
                dictionnary[letter] = 1
        return dictionnary

    def isLetterIsPresent(self, letter):
        if letter in self.mysteryWord:
            return True
        return False

    def isLetterInRightPlace(self, letter, indice):
        if self.mysteryWord[indice] == letter:
            return True
        return False

    def isDuplicate(self, letter, dictInputOccurence):
        if self.originNumberOccurence[letter] != dictInputOccurence[letter]:
            return True
        return False

    def updateOccurenceLeft(self, letter, dictio):
        dictio[letter] = dictio[letter] - 1
        return dictio

    def checkLetters(self, str):
        self.colors = []
        dictInputOccurence = self.getDicNumberOfOccurence(str)
        i = len(str) - 1
        while i >= 0:
            letter = str[i]
            if self.isLetterIsPresent(letter):
                if self.isLetterInRightPlace(letter, i):
                    self.colors.append(asciiArt.Color.RED)
                elif self.isDuplicate(letter, dictInputOccurence):
                    dictInputOccurence = self.updateOccurenceLeft(
                        letter, dictInputOccurence
                    )

                    self.colors.append(asciiArt.Color.BLUE)
                else:
                    self.colors.append(asciiArt.Color.YELLOW)
            else:
                self.colors.append(asciiArt.Color.BLUE)
            i -= 1
        self.colors = self.colors[::-1]
        self.ascii.painting(str, self.colors)
        if self.mysteryWord == str:
            self.ascii.painting("YOU WIN", None)
            sys.exit(0)

    def isWin(self, str):
        if self.mysteryWord == str:
            return True
        return False

    def isGameOver(self):
        if self.live == 6:
            return True
        return False

    def gameLoop(self):
        self.checkLetters(self.wordIndice)
        while self.isGameOver() != True:
            input_text = input(
                f"Veuillez entrer un mot commençant par la lettre : {self.mysteryWord[0]} et faisant {len(self.mysteryWord)} lettres\n"
            )
            if input_text:
                try:
                    userInput = input_text.upper()
                    self.checkRules(userInput)
                    self.checkLetters(userInput)
                    self.live += 1
                except Exception as e:
                    print(e)
        self.ascii.painting("YOU LOSE", None)
        sys.exit(0)


if __name__ == "__main__":
    """"""
