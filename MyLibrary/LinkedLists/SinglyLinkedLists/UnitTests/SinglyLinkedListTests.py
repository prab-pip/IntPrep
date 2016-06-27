import unittest

from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList

class TestSinglyLinkedListPopulate(unittest.TestCase):

    def test_populate(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(20)
        singlyLinkedListObject.populate(inputList)
        outputList = singlyLinkedListObject.returnLinkedListAsList()

        self.assertTrue(inputList == outputList, "Input List: %s and Output List: %s don't match" %(inputList, outputList))

class TestSinglyLinkedListDelete(unittest.TestCase):

    def test_delete_head_on_empty_list(self):
        singlyLinkedListObject = SinglyLinkedList()
        self.assertTrue(singlyLinkedListObject.deleteHead(), "With no elements in the list, it should return True")
        outputList = singlyLinkedListObject.returnLinkedListAsList()
        self.assertTrue(len(outputList) == 0, "Output list from an Empty Linked List must be empty")

    def test_delete_head_with_one_element_list(self):
        singlyLinkedListObject = SinglyLinkedList()
        singlyLinkedListObject.populate([1])

        singlyLinkedListObject.deleteHead()
        outputList = singlyLinkedListObject.returnLinkedListAsList()
        self.assertTrue(len(outputList) == 0, "After deleting the only element in the list, Output List must be empty")

    def test_delete_head_from_a_list_with_two_elements(self):
        singlyLinkedListObject = SinglyLinkedList()
        inputList = range(2)
        singlyLinkedListObject.populate(inputList)

        # Deleting the first element from the inputList. this will help in assertion
        inputList.pop(0)

        singlyLinkedListObject.deleteHead()
        outputList = singlyLinkedListObject.returnLinkedListAsList()
        self.assertTrue(inputList == outputList, "Expecting one lesser value in the Output List but got different. Expected: %s, Got: %s" %(inputList, outputList))

        self.assertTrue(singlyLinkedListObject.head == singlyLinkedListObject.tail, "Tail and Head must be the same after only 1 element remains in the list")

    def test_delete_head_from_a_list_with_more_than_two_elements(self):
        singlyLinkedListObject = SinglyLinkedList()
        inputList = range(20)
        singlyLinkedListObject.populate(inputList)

        # Deleting the first element from the inputList. this will help in assertion
        inputList.pop(0)

        singlyLinkedListObject.deleteHead()
        outputList = singlyLinkedListObject.returnLinkedListAsList()
        self.assertTrue(inputList == outputList, "Expecting one lesser value in the Output List but got different. Expected: %s, Got: %s" %(inputList, outputList))

        self.assertTrue(singlyLinkedListObject.head != singlyLinkedListObject.tail, "Tail and Head must NOT be the same after only 1 element remains in the list")

class TestSinglyLinkedListAppend(unittest.TestCase):

    def test_append_when_list_is_empty(self):
        singlyLinkedListObject = SinglyLinkedList()
        inputVal = 10
        singlyLinkedListObject.appendToListUsingTail(inputVal)
        outputList = singlyLinkedListObject.returnLinkedListAsList()
        outputVal = outputList[0]

        self.assertTrue(inputVal == outputVal, "Expected a tail value of: %s, Got: %s" %(inputVal, outputVal))

    def test_append_when_list_has_at_least_one_element(self):
        singlyLinkedListObject = SinglyLinkedList()
        inputList = range(10)
        singlyLinkedListObject.populate(inputList)

        inputVal = 10
        singlyLinkedListObject.appendToListUsingTail(inputVal)

        self.assertTrue(singlyLinkedListObject.tail.data == inputVal, "Expected Tail data: %s, Got: %s" %(inputVal, singlyLinkedListObject.tail.data))

        outputList = singlyLinkedListObject.returnLinkedListAsList()
        outputVal = outputList[-1]
        self.assertTrue(inputVal == outputVal, "Expected tail value: %s, Got: %s" %(inputVal, outputVal))


class TestSinglyLinkedListasPythonGenerator(unittest.TestCase):
    def test_list_as_generator(self):

        singlyLinkedListObject = SinglyLinkedList()
        inputList = range(10,100,10)
        singlyLinkedListObject.populate(inputList)
        for index, data in enumerate(singlyLinkedListObject):
            self.assertTrue(data == inputList[index], "Data mismatch. Expected data: %s, Got: %s" %(inputList[index], data))