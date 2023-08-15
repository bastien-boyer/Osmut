import random
import tracemalloc


FILE_LIST = "./liste.txt"

class Words:
    def __init__(self, word):
        self.word = word
        self.size = len(word)
        self.availableList = self.getAvailableList(self.word[0], self.size)
    
    def getAvailableList(self, letter, size):
        availableList = []
        with open(FILE_LIST , "r") as liste: 
            for word in liste:
                if word[0] == letter and len(word.strip()) == size:
                    availableList.append(word.strip())
        return availableList
                        
    
def getRandomNumber():
    return random.randint(0, 386263)

def selectWord(fileListe, random):
    liste = open(fileListe, "r")
    tracemalloc.start()

    i = 0
    for i, item in enumerate(liste):
        if i == random:
            liste.close()
            return item.rstrip("\n")


def selectListAvailable(fileListe, word):
    return 1

if __name__ == '__main__':
    """
    randomInt =  random.randint(0, 386263)
    words = Words(selectWord(FILE_LIST, 512))
    print(words.word)
    print(words.size)
    print(len(words.availableList))
    """