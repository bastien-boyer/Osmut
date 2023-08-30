import sys
import os

# Ajouter le chemin absolu du répertoire 'scripts' à sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
sys.path.append(scripts_dir)

import game
import unittest
import chooseWord
from asciiArt import Color

FILE_LIST = "./filesReference/wordReferences.txt"

class TestGameMethods(unittest.TestCase):

    def test_wordStartsWithRightLetter(self):
        gameTest = game.Game("AZERTY", None)
        with self.assertRaises(Exception) as context:
            gameTest.checkRules("ytreza")
        self.assertTrue("Le mot doit obligatoirement commencer par la lettre [A]" in str(context.exception))

    def test_wordSize(self):
        gameTest = game.Game("BONJOUR", None)
        with self.assertRaises(Exception) as context:
             gameTest.checkRules("BONJ")
        self.assertTrue(f"Le mot doit obligatoirement comporter [{len(gameTest.mysteryWord)}] lettres" in str(context.exception))

    def test_wordInDictionnary(self):
        badInput = "bgytfcs"
        word = chooseWord.ChooseWords("BONJOUR", FILE_LIST)
        gameTest = game.Game("BONJOUR", word.availableList)
        with self.assertRaises(Exception) as context:
             gameTest.checkRules(badInput.upper())
        self.assertTrue(f"Le mot '{badInput.upper()}' n'est pas dans le dictionnaire" in str(context.exception))

    def test_letterAtWrongPosition(self):
        availableList = ('TASK', 'TKAS' ,'TSAA','KAAS', 'AAAA')
        gameTest = game.Game("TASK", availableList)

        gameTest.checkLetters('TKAS')
        expectedColors = [Color.RED, Color.YELLOW, Color.YELLOW, Color.YELLOW]
        self.assertTrue(compareEnumList(expectedColors, gameTest.colors))
        
        gameTest.checkLetters('KAAS')
        expectedColors = [Color.YELLOW, Color.RED, Color.BLUE, Color.YELLOW]
        self.assertTrue(compareEnumList(expectedColors, gameTest.colors))
       
        gameTest.checkLetters('TSAA')
        expectedColors = [Color.RED, Color.YELLOW, Color.YELLOW, Color.BLUE]
        self.assertTrue(compareEnumList(expectedColors, gameTest.colors))

        gameTest.checkLetters('AAAA')
        expectedColors = [Color.BLUE, Color.RED, Color.BLUE, Color.BLUE]
        self.assertTrue(compareEnumList(expectedColors, gameTest.colors))

        gameTest = game.Game("TATA", availableList)
        gameTest.checkLetters('AAAA')
        expectedColors = [Color.BLUE, Color.RED, Color.BLUE, Color.RED]
        self.assertTrue(compareEnumList(expectedColors, gameTest.colors))                  

        gameTest = game.Game("TATA", availableList)
        gameTest.checkLetters('AAAZ')
        expectedColors = [Color.YELLOW, Color.RED, Color.BLUE, Color.BLUE]
        self.assertTrue(compareEnumList(expectedColors, gameTest.colors)) 


def compareEnumList(list1, list2):
    if len(list1) != len(list2):
        return False
    for i, enumValue1 in enumerate(list1):
        enumValue2 = list2[i]
        if enumValue2.value != enumValue1.value:
            return False
    return True

if __name__ == '__main__':
    unittest.main()