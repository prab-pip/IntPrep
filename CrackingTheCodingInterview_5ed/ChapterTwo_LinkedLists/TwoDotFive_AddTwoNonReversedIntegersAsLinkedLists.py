class Solution(object):
    """
    This solution assumes that the data in each linked list node is integer.
    """
    def __init__(self):
        pass

    def addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(self, list1CurrentNode, list2CurrentNode, outputList, firstListCount=0, secondListCount=0):

        if list1CurrentNode is None and list2CurrentNode is None:
            return (firstListCount, secondListCount, 0)
        elif list1CurrentNode is None and list2CurrentNode is not None:
            numOperationsAllowedOnList1, numOperationsAllowedOnList2, carryFromPreviousAdd = self.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(list1CurrentNode, list2CurrentNode.nextPointer, outputList, firstListCount, secondListCount+1)
        elif list1CurrentNode is not None and list2CurrentNode is None:
            numOperationsAllowedOnList1, numOperationsAllowedOnList2, carryFromPreviousAdd = self.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(list1CurrentNode.nextPointer, list2CurrentNode, outputList, firstListCount+1, secondListCount)
        else:  # Both lists' current nodes are not None. Best Case
            numOperationsAllowedOnList1, numOperationsAllowedOnList2, carryFromPreviousAdd = self.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(list1CurrentNode.nextPointer, list2CurrentNode.nextPointer, outputList, firstListCount+1, secondListCount+1)

        # print 'here??', numOperationsAllowedOnList1, numOperationsAllowedOnList2

        if numOperationsAllowedOnList1 != 0 and numOperationsAllowedOnList2 != 0:
            # print "list1CurrentNode.data: %s, list2CurrentNode.data: %s" % (list1CurrentNode.data, list2CurrentNode.data )
            sum = list1CurrentNode.data + list2CurrentNode.data + carryFromPreviousAdd
        elif numOperationsAllowedOnList1 == 0:  # Just check whats on second list
            sum = list2CurrentNode.data + carryFromPreviousAdd
        elif numOperationsAllowedOnList2 == 0:  # Just check whats on first list
            sum = list1CurrentNode.data + carryFromPreviousAdd

        data = sum%10
        carry = sum/10
        outputList.insertAtHead(data)

        if carry != 0 and (numOperationsAllowedOnList1 - 1 == 0 or numOperationsAllowedOnList2 - 1 == 0):
            # Take care of the left-over carry from the last step
            outputList.insertAtHead(carry)
        if numOperationsAllowedOnList1 == 0 and numOperationsAllowedOnList2 == 0:
            return numOperationsAllowedOnList1, numOperationsAllowedOnList2, carry
        elif numOperationsAllowedOnList1 != 0 and numOperationsAllowedOnList2 == 0:
            return numOperationsAllowedOnList1 - 1, numOperationsAllowedOnList2, carry
        elif numOperationsAllowedOnList1 == 0 and numOperationsAllowedOnList2 != 0:
            return numOperationsAllowedOnList1, numOperationsAllowedOnList2-1, carry
        else:
            return numOperationsAllowedOnList1-1, numOperationsAllowedOnList2-1, carry






