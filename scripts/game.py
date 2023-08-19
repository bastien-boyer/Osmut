import sys

class Game :
    def __init__(self, mysteryWord, availableList) -> None:
        self.mysteryWord = mysteryWord
        self.mysteryWordDic = self.getDictionnary(mysteryWord)
        self.availableWordList = availableList
        self.live = 0
        self.input = None


    def checkRules(self, str):
        if str[0] != self.mysteryWord[0]:
            raise Exception(f"Le mot doit obligatoirement commencer par la lettre [{self.mysteryWord[0].capitalize()}]")
        if len(str) != len(self.mysteryWord):
            raise Exception(f"Le mot doit obligatoirement comporter [{len(self.mysteryWord)}] lettres")
        if str not in self.availableWordList:
            raise Exception(f"Le mot '{str}' n'est pas dans le dictionnaire")

            
    def badLetter(self, letter):
        # Blue
        return "\033[34m" + letter + "\033[0m"
    
    def goodLetterButWrongEmplacement(self, letter):
        # Yellow
        return "\033[33m" + letter+ "\033[0m"
    
    def goodLetterInRightEmplacement(self, letter):
        # RED
        return "\033[31m" + letter + "\033[0m"

    def checkLetters(self, str):
        self.checkRules(str)
        if self.mysteryWord == str:
            print("YOU WIN !")
            sys.exit(0)
            self.live = 6
            return
        result = ""
        self.input = self.setInput(str)
        for key, value in self.input.items():
            if value in self.mysteryWordDic:
                if key in self.mysteryWordDic[value]:
                    result += self.goodLetterInRightEmplacement(value)
                else:
                    result += self.goodLetterButWrongEmplacement(value)
            else:
                result += self.badLetter(value)
        return result

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
        while self.isGameOver() != True:
            input_text = input(f"Veuillez entrer un mot commençant par la lettre : {self.mysteryWord[0]} et faisant {len(self.mysteryWord)} lettres\n")
            if input_text:
                try:
                    print(self.checkLetters(input_text.upper()))
                    self.live += 1
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    game = Game("bonjour", None)
    game.gameLoop()


