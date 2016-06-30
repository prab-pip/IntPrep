import unittest

from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList
from GeneralPreparation.LinkedLists.SinglyLinkedLists.ReverseASinglyLinkedList import Solution


class Test_ReverseASinglyLinkedList_PrintRecursive(unittest.TestCase):
    # Need to add tests to verify the print thing
    def test_reverse_an_empty_list(self):
        givenList = SinglyLinkedList() # Because it's an empty list, no need to populate it

        s = Solution()

        s.printReverseUsingRecursion(givenList.head)

    def test_reverse_a_list_with_one_element(self):
        givenList = SinglyLinkedList()
        inputList = [10]
        givenList.populate(inputList)

        s = Solution()

        s.printReverseUsingRecursion(givenList.head)

    def test_reverse_a_list_with_two_elements(self):
        givenList = SinglyLinkedList()
        inputList = [10, 20]
        givenList.populate(inputList)

        s = Solution()

        s.printReverseUsingRecursion(givenList.head)

    def test_reverse_a_list_with_many_elements(self):
        givenList = SinglyLinkedList()
        inputList = range(10,101,10)
        givenList.populate(inputList)

        s = Solution()

        s.printReverseUsingRecursion(givenList.head)

class Test_ReverseASinglyLinkedList_ReturnANewListRecursive(unittest.TestCase):
    def test_reverse_an_empty_list(self):
        givenList = SinglyLinkedList() # Because it's an empty list, no need to populate it

        s = Solution()
        outputLinkedList = SinglyLinkedList()
        s.returnReversedListUsingRecursion(givenList.head, outputLinkedList)
        inputList = []
        expectedList = inputList
        returnedList = outputLinkedList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_one_element(self):
        givenList = SinglyLinkedList()
        inputList = [10]
        givenList.populate(inputList)

        s = Solution()

        outputLinkedList = SinglyLinkedList()
        s.returnReversedListUsingRecursion(givenList.head, outputLinkedList)

        expectedList = inputList[::-1]
        returnedList = outputLinkedList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_two_elements(self):
        givenList = SinglyLinkedList()
        inputList = [10, 20]
        givenList.populate(inputList)

        s = Solution()

        outputLinkedList = SinglyLinkedList()
        s.returnReversedListUsingRecursion(givenList.head, outputLinkedList)

        expectedList = inputList[::-1]
        returnedList = outputLinkedList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_many_elements(self):
        givenList = SinglyLinkedList()
        inputList = range(10,101,10)
        givenList.populate(inputList)

        s = Solution()

        outputLinkedList = SinglyLinkedList()
        s.returnReversedListUsingRecursion(givenList.head, outputLinkedList)
        
        expectedList = inputList[::-1]
        returnedList = outputLinkedList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))