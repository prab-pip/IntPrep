import unittest

from CrackingTheCodingInterview_5ed.ChapterTwo_LinkedLists.TwoDotFive_AddTwoNonReversedIntegersAsLinkedLists import Solution
from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList

class Test_TwoDotFive_AddTwoNonReversedIntegersAsLinkedLists_Without_LeftOver_Carry_Tests(unittest.TestCase):

    def test_add_without_carry_basic_case_both_lists_empty(self):
        firstList = SinglyLinkedList()
        secondList = SinglyLinkedList()

        s = Solution()
        outputList = SinglyLinkedList()

        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)
        outputValue = outputList.returnLinkedListAsList()
        expectedValue = []

        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))

    def test_add_without_carry_basic_case_first_list_empty_second_list_has_one_element(self):
        firstList = SinglyLinkedList()
        secondList = SinglyLinkedList()

        inputValue = [1]
        secondList.populate(inputValue)

        s = Solution()
        outputList = SinglyLinkedList()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)
        outputValue = outputList.returnLinkedListAsList()
        expectedValue = inputValue

        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))

    def test_add_without_carry_basic_case_second_list_empty_first_list_has_one_element(self):
        firstList = SinglyLinkedList()
        inputValue = [1]
        firstList.populate(inputValue)

        secondList = SinglyLinkedList()

        s = Solution()
        outputList = SinglyLinkedList()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)
        outputValue = outputList.returnLinkedListAsList()
        expectedValue = inputValue

        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))

    def test_without_carry_best_case_equal_elements_one_in_length(self):
                firstList = SinglyLinkedList()
                firstList.populate([1])

                secondList = SinglyLinkedList()
                secondList.populate([2])

                outputList = SinglyLinkedList()
                s = Solution()
                s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

                outputValue = outputList.returnLinkedListAsList()

                expectedValue = [3]

                self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))

    def test_without_carry_best_case_equal_elements_two_in_length(self):
        firstList = SinglyLinkedList()
        firstList.populate([1, 1])

        secondList = SinglyLinkedList()
        secondList.populate([2, 3])

        outputList = SinglyLinkedList()
        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

        outputValue = outputList.returnLinkedListAsList()

        expectedValue = [3, 4]
        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))


    def test_without_carry_best_case_equal_elements_three_in_length(self):
        firstList = SinglyLinkedList()
        firstList.populate([1, 1, 8])

        secondList = SinglyLinkedList()
        secondList.populate([4, 3, 1])

        outputList = SinglyLinkedList()
        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

        outputValue = outputList.returnLinkedListAsList()

        expectedValue = [5, 4, 9]
        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))

    def test_add_without_carry_basic_case_second_list_empty_first_list_has_more_than_one_element(self):
        firstList = SinglyLinkedList()
        inputValue = range(10)
        firstList.populate(inputValue)

        secondList = SinglyLinkedList()

        outputList = SinglyLinkedList()

        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

        outputValue = outputList.returnLinkedListAsList()
        expectedValue = inputValue

        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))


    def test_add_without_carry_basic_case_first_list_empty_second_list_has_more_than_one_element(self):
        firstList = SinglyLinkedList()

        secondList = SinglyLinkedList()
        inputValue = range(10)
        secondList.populate(inputValue)

        outputList = SinglyLinkedList()

        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

        outputValue = outputList.returnLinkedListAsList()
        expectedValue = inputValue

        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))
#
#     def test_add_without_carry_both_lists_have_equal_items(self):
#         firstList = SinglyLinkedList()
#         firstList.populate([7,1,6])
#
#         secondList = SinglyLinkedList()
#         secondList.populate([5,9,2])
#
#
#         s = Solution(firstList, secondList)
#
#         returnLinkedList = s.addTwoReversedIntegersAsLinkedListsAndCreateNewList()
#         outputValue = returnLinkedList.returnLinkedListAsList()
#         expectedValue = [2,1,9]
#         self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))
#
#
    def test_add_without_left_over_carry_both_lists_have_unequal_items(self):
        firstList = SinglyLinkedList()
        firstList.populate([7,1,6,9])

        secondList = SinglyLinkedList()
        secondList.populate([5,9,2])

        outputList = SinglyLinkedList()
        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)
        outputValue = outputList.returnLinkedListAsList()
        expectedValue = [7,7,6,1]
        print "Expected: %s, Got: %s" %(expectedValue, outputValue)
        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))
#
#
#
#
class Test_TwoDotFive_AddTwoReversedIntegersAsLinkedLists_With_LeftOver_Carry_Tests(unittest.TestCase):
    def test_with_carry_best_case_equal_elements_one_in_length(self):
        firstList = SinglyLinkedList()
        firstList.populate([8])

        secondList = SinglyLinkedList()
        secondList.populate([2])

        outputList = SinglyLinkedList()
        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

        outputValue = outputList.returnLinkedListAsList()

        expectedValue = [1, 0]

        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))

    def test_with_carry_best_case_equal_elements_two_in_length(self):
        firstList = SinglyLinkedList()
        firstList.populate([7, 1])

        secondList = SinglyLinkedList()
        secondList.populate([6, 9])

        outputList = SinglyLinkedList()
        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

        outputValue = outputList.returnLinkedListAsList()

        expectedValue = [1, 4, 0]

        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))


    def test_with_carry_best_case_equal_elements_three_in_length(self):
        firstList = SinglyLinkedList()
        firstList.populate([6, 4, 9])

        secondList = SinglyLinkedList()
        secondList.populate([7, 7, 9])

        outputList = SinglyLinkedList()
        s = Solution()
        s.addTwoNonReversedIntegersAsLinkedListsAndCreateNewList(firstList.head, secondList.head, outputList)

        outputValue = outputList.returnLinkedListAsList()

        expectedValue = [1, 4, 2, 8]
        self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))


    #     def test_add_with_carry_both_lists_have_one_item(self):
#         firstList = SinglyLinkedList()
#         firstList.populate([9])
#
#         secondList = SinglyLinkedList()
#         secondList.populate([1])
#
#
#         s = Solution(firstList, secondList)
#
#         returnLinkedList = s.addTwoReversedIntegersAsLinkedListsAndCreateNewList()
#         outputValue = returnLinkedList.returnLinkedListAsList()
#         expectedValue = [0,1]
#         self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))
#
#     def test_add_with_carry_forever_carry_till_last(self):
#         firstList = SinglyLinkedList()
#         firstList.populate([9,9,9,9,9,9,9])
#
#         secondList = SinglyLinkedList()
#         secondList.populate([1])
#
#
#         s = Solution(firstList, secondList)
#
#         returnLinkedList = s.addTwoReversedIntegersAsLinkedListsAndCreateNewList()
#         outputValue = returnLinkedList.returnLinkedListAsList()
#         expectedValue = [0,0,0,0,0,0,0,1]
#         self.assertTrue(outputValue == expectedValue, "Expected: %s, Got: %s" %(expectedValue, outputValue))