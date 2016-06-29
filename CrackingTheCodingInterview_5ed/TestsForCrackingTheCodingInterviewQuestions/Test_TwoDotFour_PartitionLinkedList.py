import unittest

from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList
from CrackingTheCodingInterview_5ed.TwoDotFour_PartitionLinkedList import Solution


class Test_Solution_of_TwoDotFour_PartitionLinkedList_create_new_list(unittest.TestCase):
    def test_partition_number_present_in_middle_of_list(self):
        
        inputList = [38, 76, 72, 44, 17, 65, 24, 59, 47, 76]
        print inputList

        givenSinglyLinkedList = SinglyLinkedList()
        givenSinglyLinkedList.populate(inputList)

        s = Solution(givenSinglyLinkedList)

        returnList = s.partitionLinkedListBasedOnAGivenNumber_createNewList(38)
        outputList = [17, 24, 38, 76, 72, 44, 65, 59, 47, 76]

        returnedList = returnList.returnLinkedListAsList()
        self.assertTrue(returnedList == outputList, "Expected: %s, Got: %s" %(outputList, returnedList))

class Test_Solution_of_TwoDotFour_PartitionLinkedList_dont_create_new_list(unittest.TestCase):
    def test_partition_number_present_in_start_of_list(self):
        # inputList = returnRandomListOfIntegers()

        inputList = [38, 76, 72, 44, 17, 65, 24, 59, 47, 76]
        print inputList

        givenSinglyLinkedList = SinglyLinkedList()
        givenSinglyLinkedList.populate(inputList)

        s = Solution(givenSinglyLinkedList)

        returnList = s.partitionLinkedListBasedOnAGivenNumber_DontCreateNewList(38)

        outputList = [17, 24, 38, 76, 72, 44, 65, 59, 47, 76]

        returnedList = returnList.returnLinkedListAsList()
        self.assertTrue(returnedList == outputList, "Expected: %s, Got: %s" %(outputList, returnedList))