import sys
import os

# Ajouter le chemin absolu du répertoire 'scripts' à sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
sys.path.append(scripts_dir)

import extract
import unittest

class TestExtractMethods(unittest.TestCase):


    def test_randomNumber(self):
        number = extract.getRandomNumber()
        self.assertGreaterEqual(number, 0)
        self.assertLessEqual( number, 386263)


    def test_wordSelected(self):
        fileList = "./liste.txt"
        words = extract.Words(extract.selectWord(fileList, 512))
        self.assertEqual(words.word, "ABIMASSE")
        self.assertEqual(3650, len(words.availableList))




if __name__ == '__main__':
    unittest.main()