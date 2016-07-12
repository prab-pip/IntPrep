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

    def _palindromeOrNot(self, leftSideNode, length):
        if length == 0:
            return leftSideNode
        elif length == 1:
            return leftSideNode.nextPointer
        else:
            rightSideNode = self._palindromeOrNot(leftSideNode.nextPointer, length - 2)
            if rightSideNode is False:
                return False
            elif leftSideNode.data != rightSideNode.data:
                # print "not a palindrome. %s != %s" % (leftSideNode.data, rightSideNode.data)
                return False
            else:
                return rightSideNode.nextPointer


    def method2(self):
        '''
        Implementing the solution as mentioned in the CTCI book:-
        1. Get the length of the list
        2. use the value of length to judge whether we've reached the centre of the list
        3. In the base case, return the next node of the middle
        4. In the recursive case, compare the current node data vs returned node data
        '''
        length = len(self.singlyLinkedListObject)
        if length == 0:
            return True  # Considering a Linked List with zero length is a palindrome
        elif length == 1:
            return True  # A Linked List with zero length is a palindrome
        else:
            returnedStatus = self._palindromeOrNot(self.singlyLinkedListObject.head, length)
            if returnedStatus is False:
                return False
            elif returnedStatus is None:
                return True
            # Short form of  above code: return returnedStatus is None

