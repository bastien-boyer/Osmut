import sys
import os

# Ajouter le chemin absolu du répertoire 'scripts' à sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
sys.path.append(scripts_dir)

import game
import unittest
import chooseWord

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

if __name__ == '__main__':
    unittest.main()