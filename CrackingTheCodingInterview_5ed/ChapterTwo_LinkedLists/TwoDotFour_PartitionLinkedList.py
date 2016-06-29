from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList

class Solution(object):
    def __init__(self, givenSinglyLinkedList):
        self.givenSinglyLinkedList = givenSinglyLinkedList
        self.l = range(20)

    def partitionLinkedListBasedOnAGivenNumber_createNewList(self, givenNumber):
        firstList = SinglyLinkedList()
        secondList = SinglyLinkedList()

        for data in self.givenSinglyLinkedList:
            if data < givenNumber:
                firstList.appendToListUsingTail(data)
            else:
                secondList.appendToListUsingTail(data)

        # print firstList.returnLinkedListAsList()
        # print secondList.returnLinkedListAsList()

        if firstList.isListEmpty():
            return secondList
        elif secondList.isListEmpty():
            return firstList
        else:
            firstList.tail.nextPointer = secondList.head # Could be the other way round as well (secondList.tail.nextPointer = firstList.head ), but since it wasn't asked in the question, I've chosen the first option. In a real interview, I would ask the interviewer
            return firstList

    def partitionLinkedListBasedOnAGivenNumber_DontCreateNewList(self, givenNumber):
        # check head against given number. Move to appropriate list. advance head to next. delete previous head


        firstList = SinglyLinkedList()
        secondList = SinglyLinkedList()

        for data in self.givenSinglyLinkedList:
            if data < givenNumber:
                firstList.appendToListUsingTail(data)
            else:
                secondList.appendToListUsingTail(data)
            self.givenSinglyLinkedList.deleteHead() # Deleting head as the data is already under the relevant - firstList or secondList

        if firstList.isListEmpty():
            return secondList
        elif secondList.isListEmpty():
            return firstList
        else:
            firstList.tail.nextPointer = secondList.head # Could be the other way round as well (secondList.tail.nextPointer = firstList.head ), but since it wasn't asked in the question, I've chosen the first option. In a real interview, I would ask the interviewer
            return firstList
