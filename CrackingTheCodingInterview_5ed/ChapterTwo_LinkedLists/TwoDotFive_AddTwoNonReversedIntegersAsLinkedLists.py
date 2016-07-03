class Solution(object):
    """
    This solution assumes that the data in each linked list node is integer.

    # Important step for this question:-
    1. Because 2 lists could differ in length. left-fill the smaller list with zeroes
    """
    def __init__(self, list1, list2, outputList):
        self.list1 = list1
        self.list2 = list2
        self.outputList = outputList

    def insertZeroesAtHead(self, linkedListObject, numZeroes):
        for zero in xrange(numZeroes):
            linkedListObject.insertAtHead(0)

    def add_now(self, list1CurrentNode, list2CurrentNode):
        if list1CurrentNode is None:
            return 0  # Returning 0 as carry for first use
        else:
            carryReturned = self.add_now(list1CurrentNode.nextPointer, list2CurrentNode.nextPointer)

            sum = carryReturned + list1CurrentNode.data + list2CurrentNode.data

            data = sum % 10
            self.outputList.insertAtHead(data)

            carryGenerated = sum / 10
            return carryGenerated


    def addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(self):
        lenList1 = len(self.list1)
        lenList2 = len(self.list2)

        diff = lenList1 - lenList2
        if diff < 0:  # Means list1 is smaller than list2
            self.insertZeroesAtHead(self.list1, -diff)
        else:
            self.insertZeroesAtHead(self.list2, diff)

        carryReturned = self.add_now(self.list1.head, self.list2.head)
        if carryReturned != 0:
            self.outputList.insertAtHead(carryReturned)