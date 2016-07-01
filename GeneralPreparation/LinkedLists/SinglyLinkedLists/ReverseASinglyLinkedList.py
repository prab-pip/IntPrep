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

    def reverseOriginalList_Iterative(self, originalList):
        if originalList.isHeadNone():
            return
        previous = None
        while originalList.head.nextPointer is not None:
            nextNode = originalList.head.nextPointer
            originalList.head.nextPointer = previous
            previous = originalList.head
            originalList.head = nextNode

        originalList.head.nextPointer = previous

    def reverseOriginalLinkedList_Recursive(self, originalList, previousNode = None):
        if originalList.isHeadNone():
            return
        nextNode = originalList.head.nextPointer
        originalList.head.nextPointer = previousNode

        if nextNode is not None:
            previousNode = originalList.head
            originalList.head = nextNode
            self.reverseOriginalLinkedList_Recursive(originalList, previousNode)
