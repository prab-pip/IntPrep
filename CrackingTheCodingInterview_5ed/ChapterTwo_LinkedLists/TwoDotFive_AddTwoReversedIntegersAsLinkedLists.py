from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList

class Solution(object):
    """
    This solution assumes that the data in each linked list node is integer.
    """
    def __init__(self, firstList, secondList):
        self.firstList = firstList
        self.secondList = secondList

    def addTwoReversedIntegersAsLinkedListsAndCreateNewList(self):
        outputList = SinglyLinkedList()

        carry = 0
        firstListCurrentNode = self.firstList.head
        secondListCurrentNode = self.secondList.head
        while firstListCurrentNode is not None and secondListCurrentNode is not None:
            sum = carry + firstListCurrentNode.data + secondListCurrentNode.data
            data = sum%10
            carry = sum/10
            # print "data: %s" %data
            # print "carry: %s" %carry
            outputList.appendToListUsingTail(data)
            firstListCurrentNode = firstListCurrentNode.nextPointer
            secondListCurrentNode = secondListCurrentNode.nextPointer

        # there could be a left-over carry. Need to add it to the list now, but before that, need to check if the number of items in the list were uneven
        currentNode = None
        if firstListCurrentNode is None:
            currentNode = secondListCurrentNode
        else:
            currentNode = firstListCurrentNode
        # If both firstListCurrentNode and secondListCurrentNode are None, it is implicitly covered

        while currentNode is not None:
            sum = carry + currentNode.data
            data = sum%10
            carry = sum/10

            outputList.appendToListUsingTail(data)

            currentNode = currentNode.nextPointer

        # Now, check the left-over carry and add it to the list if it is non-zero
        if carry != 0:
            outputList.appendToListUsingTail(carry)




        # print outputList.returnLinkedListAsList()
        return outputList

