import sys
import os

# Ajouter le chemin absolu du répertoire 'scripts' à sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
sys.path.append(scripts_dir)

import chooseWord
import unittest

class TestExtractMethods(unittest.TestCase):

    def test_randomNumber(self):
        number = chooseWord.generate_random_with_datetime()
        self.assertGreaterEqual(number, 0)
        self.assertLessEqual( number, 152184)


    def test_wordSelectedAndAvailableList(self):
        fileList = "./wordReferences.txt"
        words = chooseWord.ChooseWords(chooseWord.selectWord(fileList, 512), fileList)
        self.assertEqual(words.chosenWord, "ABOTEAU")
        self.assertEqual(2401, len(words.availableList))




if __name__ == '__main__':
    unittest.main()