class WordReference:

    """
    Transform a list of Scrabble words into a reference list. The words must be in the French dictionary and have between 6 and 9 letters.
    """

    def __init__(self) -> None:
        pass

    def populateWordListReference(self, fileList):
        tmp = open(fileList, "r")
        wordReferenceTxt = open("./wordReferences.txt", "w")

        for word in tmp:
            wordSize = len(word.strip())
            if wordSize >= 6 and wordSize <= 9:
                wordReferenceTxt.write(word)
        tmp.close()
        wordReferenceTxt.close()


if __name__ == "__main__":
    word = WordReference()
