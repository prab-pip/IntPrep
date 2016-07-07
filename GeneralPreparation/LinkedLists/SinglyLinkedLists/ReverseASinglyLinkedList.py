class Solution(object):
    def __init__(self):
        pass

    def printReverseUsingRecursion(self, listHead):
        if listHead is not None:
            self.printReverseUsingRecursion(listHead.nextPointer)
            print listHead.data

    def yieldListDataInReversedOrderUsingRecursion(self, listHead):
            # # print 'called', listHead.data
            # if listHead is None:  # Fail safe
            #     yield None
            # elif listHead.nextPointer is None:
            #     print 'fdfd'
            #     yield listHead  # This will return the tail
            # elif listHead.nextPointer is not None:  # Recursive step
            #     # print 'here: ', listHead.data, listHead.nextPointer.data
            #     print 'e'
            #     for i in self.yieldListDataInReversedOrderUsingRecursion(listHead.nextPointer):
            #         yield i
            #     # print 'aaaaa', listHead.data
            #     # yield listHead.data
            # # else:
            # #     # print 'not coming here??'

        return "This is not implemented yet, because I need to work on recursive generator functions."


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
