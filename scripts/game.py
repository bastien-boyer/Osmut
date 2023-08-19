import sys
from scripts import asciiArt

class Game :
    def __init__(self, mysteryWord, availableList) -> None:
        self.mysteryWord = mysteryWord
        self.mysteryWordDic = self.getDictionnary(mysteryWord)
        self.availableWordList = availableList
        self.live = 0
        self.input = None
        self.color = []
        self.ascii = asciiArt.AsciiArt()
        self.wordIndice = self.createWordIndice()


    def createWordIndice(self):
        tmp = ""
        for i, letter in enumerate(self.mysteryWord):
            if i == 0:
                tmp += self.mysteryWord[i]
            else:
                tmp += '_'
        return tmp

    def checkRules(self, str):
        if str[0] != self.mysteryWord[0]:
            raise Exception(f"Le mot doit obligatoirement commencer par la lettre [{self.mysteryWord[0].capitalize()}]")
        if len(str) != len(self.mysteryWord):
            raise Exception(f"Le mot doit obligatoirement comporter [{len(self.mysteryWord)}] lettres")
        if str not in self.availableWordList:
            raise Exception(f"Le mot '{str}' n'est pas dans le dictionnaire")

            
 
    def checkLetters(self, str):
        result = ""
        self.input = self.setInput(str)
        self.color = []
        for key, value in self.input.items():
            if value in self.mysteryWordDic:
                if key in self.mysteryWordDic[value]:
                    result += value
                    self.color.append(asciiArt.Color.RED)
                else:
                    result += value
                    self.color.append(asciiArt.Color.YELLOW)

            else:
                result += value                
                self.color.append(asciiArt.Color.BLUE)
        self.ascii.painting(result, self.color)
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
        
    def setInput(self, str):
        dictionnary = {}
        for index, letter in enumerate(str):
            dictionnary[index] = letter
        return dictionnary
        
    def getDictionnary(self, word):
        dictionnary = {}
        for index, letter in enumerate(word):
            if letter in dictionnary:
                dictionnary[letter].append(index)
            else:
                dictionnary[letter] = [index]
        return dictionnary

    def gameLoop(self):
        print(f"{self.mysteryWord}")
        self.checkLetters(self.wordIndice)
        while self.isGameOver() != True:
            input_text = input(f"Veuillez entrer un mot commençant par la lettre : {self.mysteryWord[0]} et faisant {len(self.mysteryWord)} lettres\n")
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


if __name__ == '__main__':
    game = Game("bonjour", None)
    game.gameLoop()
