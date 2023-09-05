from scripts import chooseWord, game

FILE_LIST = "./filesReference/wordReferences.txt"


def main():
    words = chooseWord.ChooseWords(
        chooseWord.selectWord(FILE_LIST, chooseWord.generate_random_with_datetime()),
        FILE_LIST,
    )
    game.Game(words.chosenWord, words.availableList).gameLoop()


if __name__ == "__main__":
    main()
