import unittest

from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList
from CrackingTheCodingInterview_5ed.ChapterTwo_LinkedLists.TwoDotSix_ReturnNodeAtBeginingOfLinkedListLoop import Solution

class Test_ReturnNodeAtBeginingOfLinkedListLoop(unittest.TestCase):
    def test_returnNodeAtBeginingOfLinkedListLoop(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(1,12)
        singlyLinkedListObject.populate(inputList)

        s = Solution(singlyLinkedListObject)

        # Insert a loop at 4th position
        singlyLinkedListObject.tail.nextPointer = singlyLinkedListObject.head.nextPointer.nextPointer.nextPointer

        s.returnNodeAtBeginingOfLinkedListLoop()


