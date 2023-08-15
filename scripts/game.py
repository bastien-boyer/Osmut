

class Game :
    def __init__(self, mysteryWord, wordList) -> None:
        self.mysteryWord = mysteryWord
        self.mysteryWordDic = self.getDictionnary(mysteryWord)
        self.wordList = wordList
        self.live = 0
        self.input = None


    def checkRules(self, str):
        if str[0] != self.mysteryWord[0]:
            raise Exception(f"Le mot doit obligatoirement commencer par la lettre [{self.mysteryWord[0].capitalize()}]")
        if len(str) != len(self.mysteryWord):
            raise Exception(f"Le mot doit obligatoirement comporter [{len(self.mysteryWord)}] lettres")
            

    def checkLetters(self, str):
        self.checkRules(str)
        if self.mysteryWord == str:
            print("YOU WIN !")
            self.live = 6
            return
        result = ""
        self.input = self.setInput(str)
        for key, value in self.input.items():
            if value in self.mysteryWordDic:
                if key in self.mysteryWordDic[value]:
                    result += "\033[31m" + value.capitalize() + "\033[0m"
                else:
                    result += "\033[33m" + value.capitalize() + "\033[0m"
            else:
                result += "\033[34m" + value.capitalize() + "\033[0m"
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
        while game.isGameOver() != True:
            input_text = input("Veuillez entrer une valeur : ")
            if input_text:
                try:
                    print(self.checkLetters(input_text))
                    self.live += 1
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    game = Game("bonjour", None)
    game.gameLoop()


