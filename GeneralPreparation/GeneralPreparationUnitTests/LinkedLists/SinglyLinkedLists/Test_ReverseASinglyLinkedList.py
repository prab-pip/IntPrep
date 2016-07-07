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

class Test_ReverseASinglyLinkedList_ReverseOriginalListIterative(unittest.TestCase):
    def test_reverse_an_empty_list(self):
        originalList = SinglyLinkedList() # Because it's an empty list, no need to populate it

        s = Solution()
        s.reverseOriginalList_Iterative(originalList)

        inputList = []
        expectedList = inputList
        returnedList = originalList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_one_element(self):
        originalList = SinglyLinkedList()
        inputList = [10]
        originalList.populate(inputList)

        s = Solution()

        s.reverseOriginalList_Iterative(originalList)

        expectedList = inputList[::-1]
        returnedList = originalList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_two_elements(self):
        originalList = SinglyLinkedList()
        inputList = [10, 20]
        originalList.populate(inputList)

        s = Solution()

        s.reverseOriginalList_Iterative(originalList)

        expectedList = inputList[::-1]
        returnedList = originalList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_many_elements(self):
        originalList = SinglyLinkedList()
        inputList = range(10,101,10)
        originalList.populate(inputList)

        s = Solution()

        s.reverseOriginalList_Iterative(originalList)

        expectedList = inputList[::-1]
        returnedList = originalList.returnLinkedListAsList()

        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

class Test_ReverseASinglyLinkedList_ReverseOriginalListRecursive(unittest.TestCase):
    def test_reverse_an_empty_list(self):
        originalList = SinglyLinkedList() # Because it's an empty list, no need to populate it

        s = Solution()
        s.reverseOriginalLinkedList_Recursive(originalList)

        inputList = []
        expectedList = inputList
        returnedList = originalList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_one_element(self):
        originalList = SinglyLinkedList()
        inputList = [10]
        originalList.populate(inputList)

        s = Solution()

        s.reverseOriginalLinkedList_Recursive(originalList)

        expectedList = inputList[::-1]
        returnedList = originalList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_two_elements(self):
        originalList = SinglyLinkedList()
        inputList = [10, 20]
        originalList.populate(inputList)

        s = Solution()

        s.reverseOriginalLinkedList_Recursive(originalList)

        expectedList = inputList[::-1]
        returnedList = originalList.returnLinkedListAsList()
        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

    def test_reverse_a_list_with_many_elements(self):
        originalList = SinglyLinkedList()
        inputList = range(10,101,10)
        originalList.populate(inputList)

        s = Solution()

        s.reverseOriginalLinkedList_Recursive(originalList)

        expectedList = inputList[::-1]
        returnedList = originalList.returnLinkedListAsList()

        self.assertTrue(expectedList == returnedList, "Expected: %s, Got: %s" %(expectedList, returnedList))

class Test_ReverseASinglyLinkedList_yieldListDataInReversedOrderUsingRecursion(unittest.TestCase):
    def test_yield_reverse_empty_list(self):
        singlyLinkedListObject = SinglyLinkedList()

        s = Solution()
        for i in s.yieldListDataInReversedOrderUsingRecursion(singlyLinkedListObject.head):
            print i

    def test_yield_reverse_list_with_one_element(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = [1]
        singlyLinkedListObject.populate(inputList)

        s = Solution()

        for i in s.yieldListDataInReversedOrderUsingRecursion(singlyLinkedListObject.head):
            print i

    def test_yield_reverse_list_with_two_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = [1, 2]
        singlyLinkedListObject.populate(inputList)

        s = Solution()

        for i in s.yieldListDataInReversedOrderUsingRecursion(singlyLinkedListObject.head):
            print i

    def test_yield_reverse_list_with_three_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = [1, 2, 3]
        singlyLinkedListObject.populate(inputList)

        s = Solution()

        for i in s.yieldListDataInReversedOrderUsingRecursion(singlyLinkedListObject.head):
            print i