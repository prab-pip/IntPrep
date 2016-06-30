class Solution(object):
    def __init__(self, givenList = None):
        pass

    def printReverseUsingRecursion(self, listHead):
        if listHead is not None:
            self.printReverseUsingRecursion(listHead.nextPointer)
            print listHead.data

    def returnReversedListUsingRecursion(self, inputListHead, outputList):
        if inputListHead is not None:
            self.returnReversedListUsingRecursion(inputListHead.nextPointer, outputList)
            outputList.appendToListUsingTail(inputListHead.data)

