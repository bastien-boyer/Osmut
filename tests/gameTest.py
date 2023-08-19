import sys
import os

# Ajouter le chemin absolu du répertoire 'scripts' à sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
sys.path.append(scripts_dir)

import game
import unittest


class TestGameMethods(unittest.TestCase):
    wordList = "./wordReference.txt"

    def test_wordStartsWithRightLetter(self):
        gameTest = game.Game("AZERTY", None)
        with self.assertRaises(Exception) as context:
            gameTest.checkLetters("ytreza")
        self.assertTrue("Le mot doit obligatoirement commencer par la lettre [A]" in str(context.exception))

    def test_wordSize(self):
        gameTest = game.Game("BONJOUR", None)
        with self.assertRaises(Exception) as context:
             gameTest.checkLetters("BONJ")
        self.assertTrue(f"Le mot doit obligatoirement comporter [{len(gameTest.mysteryWord)}] lettres" in str(context.exception))

    def test_wordInDictionnary(self):
        badInput = "bgytfcs"
        gameTest = game.Game("BONJOUR", self.wordList)
        with self.assertRaises(Exception) as context:
             gameTest.checkLetters(badInput.upper())
        self.assertTrue(f"Le mot '{badInput.upper()}' n'est pas dans le dictionnaire" in str(context.exception))

if __name__ == '__main__':
    unittest.main()