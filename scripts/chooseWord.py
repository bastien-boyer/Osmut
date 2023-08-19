import random
import datetime
import os
import struct
import tracemalloc


class ChooseWords:
    def __init__(self, word, wordReferenceList):
        self.chosenWord = word.upper()
        self.size = len(word)
        self.availableList = self.getAvailableList(self.chosenWord[0], self.size, wordReferenceList)

    
    def getAvailableList(self, letter, size, wordReferenceList):
        availableList = []
        with open(wordReferenceList , "r") as liste: 
            for word in liste:
                if word[0] == letter and len(word.strip()) == size:
                    availableList.append(word.strip())
        return availableList
                        


def generate_random_with_datetime():
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.timestamp()  # Convertit le datetime en un nombre flottant
    seed = int(timestamp * 1000000)  # Convertit le flottant en un entier

    random.seed(seed)  # Utilise l'entier comme graine

    random_number = random.randint(0, 152184)
    return random_number


def selectWord(wordReferenceList, random):
    liste = open(wordReferenceList, "r")
    tracemalloc.start()

    for i, item in enumerate(liste):
        if i == random:
            liste.close()
            return item.rstrip("\n")


if __name__ == '__main__':
   """"""