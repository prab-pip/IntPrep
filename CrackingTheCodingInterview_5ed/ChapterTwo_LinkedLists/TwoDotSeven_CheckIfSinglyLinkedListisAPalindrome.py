from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList
from GeneralPreparation.LinkedLists.SinglyLinkedLists import ReverseASinglyLinkedList

class Solution(object):
    def __init__(self, singlyLinkedListObject):
        self.singlyLinkedListObject = singlyLinkedListObject

    def method1(self):
        '''
        1. Go to the centre of the list using the slow and fast pointer approach
        2. Create another reversed list starting from the second half
        3. Compare this new list with the original list head and stop when the new list hits None
        :return: Boolean
        '''
        centreOfLinkedList = self.singlyLinkedListObject.returnCentreOfTheLinkedList()
        if centreOfLinkedList is None:
            # print "Empty List is a palindrome"
            return True

        newHalfList = SinglyLinkedList()
        newHalfList.populateNewListStartingFromALinkedListNode(centreOfLinkedList.nextPointer)

        #Reversing
        ReverseASinglyLinkedList.Solution().reverseOriginalList_Iterative(newHalfList)

        originalListCurrentNode = self.singlyLinkedListObject.head
        for dataFromSecondHalf in newHalfList:
            if originalListCurrentNode.data != dataFromSecondHalf:
                # print "Not a palindrome"
                return False
            originalListCurrentNode = originalListCurrentNode.nextPointer

        # print "Linked List is a palindrome"
        return True