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

class TestSinglyLinkedListLength(unittest.TestCase):
    def test_length_of_empty_list(self):
        singlyLinkedListObject = SinglyLinkedList()

        expectedLength = 0
        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

    def test_length_of_list_with_one_element(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(1)
        singlyLinkedListObject.populate(inputList)

        expectedLength = len(inputList)

        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

    def test_length_of_list_with_two_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(2)
        singlyLinkedListObject.populate(inputList)

        expectedLength = len(inputList)

        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

    def test_length_of_list_with_many_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(100000)
        singlyLinkedListObject.populate(inputList)

        expectedLength = len(inputList)

        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

    def test_length_of_list_after_list_change_operations(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(10)
        singlyLinkedListObject.populate(inputList)

        expectedLength = len(inputList)

        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

        singlyLinkedListObject.deleteHead()

        expectedLength -= 1

        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

        singlyLinkedListObject.insertAtHead(200)
        expectedLength += 1

        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))


        singlyLinkedListObject.insertAtHead(200)
        expectedLength += 1

        actualLength = len(singlyLinkedListObject)

        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

    def test_changing_list_length_during_append_operation(self):
        singlyLinkedListObject = SinglyLinkedList()

        expectedLength = 0
        actualLength = len(singlyLinkedListObject)
        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

        inputList = range(10)
        for data in inputList:
            singlyLinkedListObject.appendToListUsingTail(data)

            actualLength = len(singlyLinkedListObject)
            expectedLength += 1  # Because a new element has been added to the list.
            self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

    def test_changing_list_length_during_insert_at_head_operation(self):
        singlyLinkedListObject = SinglyLinkedList()

        expectedLength = 0
        actualLength = len(singlyLinkedListObject)
        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

        inputList = range(10)
        for data in inputList:
            singlyLinkedListObject.insertAtHead(data)

            actualLength = len(singlyLinkedListObject)
            expectedLength += 1  # Because a new element has been added to the list.
            self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

    def test_changing_list_length_during_delete_head_operation(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(10)
        singlyLinkedListObject.populate(inputList)

        expectedLength = len(inputList)
        actualLength = len(singlyLinkedListObject)
        self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))

        for data in inputList:
            singlyLinkedListObject.deleteHead()

            actualLength = len(singlyLinkedListObject)
            expectedLength -= 1  # Because a new element has been added to the list.
            self.assertTrue(expectedLength == actualLength, "Expected length: %s, Actual Length: %s" %(expectedLength, actualLength))


class TestDeleteHeadOperation(unittest.TestCase):
    def test_delete_head_of_empty_list(self):
        singlyLinkedListObject = SinglyLinkedList()

        singlyLinkedListObject.deleteHead()
        self.assertTrue(singlyLinkedListObject.isHeadNone(), "Head of empty list must be None")

    def test_delete_head_of_empty_list_more_than_once(self):
        singlyLinkedListObject = SinglyLinkedList()

        singlyLinkedListObject.deleteHead()
        self.assertTrue(singlyLinkedListObject.isHeadNone(), "Head of empty list must be None")

        singlyLinkedListObject.deleteHead()
        self.assertTrue(singlyLinkedListObject.isHeadNone(), "Head of empty list must be None")

        singlyLinkedListObject.deleteHead()
        self.assertTrue(singlyLinkedListObject.isHeadNone(), "Head of empty list must be None")

    def test_delete_head_of_list_with_one_item(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = [1]
        singlyLinkedListObject.populate(inputList)

        singlyLinkedListObject.deleteHead()
        self.assertTrue(singlyLinkedListObject.isHeadNone(), "Now that the only element in the list is deleted, Head of empty list must be None")

        singlyLinkedListObject.deleteHead()
        self.assertTrue(singlyLinkedListObject.isHeadNone(), "Now that the only element in the list is deleted, Head of empty list must be None")

    def test_delete_head_of_list_with_more_than_one_item(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = [1, 2, 3]
        singlyLinkedListObject.populate(inputList)

        singlyLinkedListObject.deleteHead()
        self.assertFalse(singlyLinkedListObject.isHeadNone(), "Head of non-empty list must NOT be None")
        self.assertFalse(singlyLinkedListObject.head == 2, "Expected hea data: %s, Actual head data: %s" %(2, singlyLinkedListObject.head))

        singlyLinkedListObject.deleteHead()
        self.assertFalse(singlyLinkedListObject.isHeadNone(), "Head of non-empty list must NOT be None")

        self.assertFalse(singlyLinkedListObject.head == 3, "Expected hea data: %s, Actual head data: %s" %(3, singlyLinkedListObject.head))


        singlyLinkedListObject.deleteHead()
        self.assertTrue(singlyLinkedListObject.isHeadNone(), "Head of Empty list must be None")


class TestCentreOfTheLinkedList(unittest.TestCase):
    def test_return_centre_of_empty_list(self):
        singlyLinkedListObject = SinglyLinkedList()
        expectedCentre = None
        actualCentre = singlyLinkedListObject.returnCentreOfTheLinkedList()
        self.assertTrue(expectedCentre == actualCentre, "Expected centre if linked list: %s, Got: %s" %(expectedCentre, actualCentre))

    def test_return_centre_of_list_with_one_element(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(1)
        singlyLinkedListObject.populate(inputList)

        centreIndex = (len(inputList)-1)/2
        expectedCentre = inputList[centreIndex]

        actualCentre = singlyLinkedListObject.returnCentreOfTheLinkedList()
        self.assertTrue(expectedCentre == actualCentre.data, "Expected centre if linked list: %s, Got: %s" %(expectedCentre, actualCentre))

    def test_return_centre_of_list_with_two_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(2)
        singlyLinkedListObject.populate(inputList)

        centreIndex = (len(inputList)-1)/2
        expectedCentre = inputList[centreIndex]

        actualCentre = singlyLinkedListObject.returnCentreOfTheLinkedList()
        self.assertTrue(expectedCentre == actualCentre.data, "Expected centre if linked list: %s, Got: %s" %(expectedCentre, actualCentre))

    def test_return_centre_of_list_with_third_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(3)
        singlyLinkedListObject.populate(inputList)

        centreIndex = (len(inputList)-1)/2
        expectedCentre = inputList[centreIndex]

        actualCentre = singlyLinkedListObject.returnCentreOfTheLinkedList()
        print "Expected centre if linked list: %s, Got: %s" %(expectedCentre, actualCentre)
        self.assertTrue(expectedCentre == actualCentre.data, "Expected centre if linked list: %s, Got: %s" %(expectedCentre, actualCentre))


    def test_return_centre_of_list_with_many_odd_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(20001)
        singlyLinkedListObject.populate(inputList)

        centreIndex = (len(inputList)-1)/2
        expectedCentre = inputList[centreIndex]

        actualCentre = singlyLinkedListObject.returnCentreOfTheLinkedList()
        self.assertTrue(expectedCentre == actualCentre.data, "Expected centre if linked list: %s, Got: %s" %(expectedCentre, actualCentre))

    def test_return_centre_of_list_with_many_even_elements(self):
        singlyLinkedListObject = SinglyLinkedList()

        inputList = range(40000)
        singlyLinkedListObject.populate(inputList)

        centreIndex = (len(inputList)-1)/2
        expectedCentre = inputList[centreIndex]

        actualCentre = singlyLinkedListObject.returnCentreOfTheLinkedList()
        self.assertTrue(expectedCentre == actualCentre.data, "Expected centre if linked list: %s, Got: %s" %(expectedCentre, actualCentre))