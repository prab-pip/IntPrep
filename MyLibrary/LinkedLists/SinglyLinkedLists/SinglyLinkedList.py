from SinglyLinkedListNode import SinglyLinkedListNode

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def isListEmpty(self):
        return self.isHeadNone() and self.isTailNone()

    def isHeadNone(self):
        return self.head is None

    def isTailNone(self):
        return self.tail is None

    def populate(self, listOfDataValues):
        if not self.isHeadNone():
            raise Exception("Already has some data")
        self.head = SinglyLinkedListNode(listOfDataValues[0])
        self.tail = self.head

        self.temp = self.head
        for dataValue in listOfDataValues[1:]:
            self.listNode = SinglyLinkedListNode(dataValue)
            self.temp.nextPointer = self.listNode
            self.temp = self.temp.nextPointer

        self.tail = self.temp

    def iterateSinglyLinkedList(self):
        self.temp = self.head
        while(self.temp is not None):
            print self.temp.data
            self.temp = self.temp.nextPointer

    def returnLinkedListAsList(self):
        returnList = []

        self.temp = self.head
        while(self.temp is not None):
            returnList.append(self.temp.data)
            self.temp = self.temp.nextPointer

        return returnList


    def deleteHead(self):
        '''
        cases-
        1. head is already none
        2. list has only 1 element, so tail and head are same. need to handle tail case as well
        3. list has > 1 element. So, head and tail are different. Only need to change head. No need to touch head
        :return:
        '''

        if self.isHeadNone():
            return True
        elif self.head == self.tail: # Means there is only 1 element in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nextPointer


    def delete_all(self):
        while not self.isHeadNone():
            self.deleteHead()

    def appendToListUsingTail(self, data):
        self.tempNode = SinglyLinkedListNode(data)

        if self.tail is None: # Meaning append is called when list is empty
            self.head = self.tail = self.tempNode
        else: # Meaning there is at least one element already in the list
            self.tail.nextPointer = self.tempNode
            self.tail = self.tempNode

    def __iter__(self):
        '''
        Iterate over the singly linked list. Very useful, but must be used carefully.
        If list is already deleted, or some node is already deleted, this can cause some confusion, as the reference to the currentNode will still be active. So, it wont be garbage collected.
        :return: None
        '''
        self.currentNode = self.head
        while self.currentNode is not None:
            yield self.currentNode.data
            self.currentNode = self.currentNode.nextPointer

    def insertAtHead(self, data):
        self.tempNode = SinglyLinkedListNode(data)


        if self.isHeadNone():# Make tempNode as head as well as tail
            self.head = self.tail = self.tempNode
        else:
            self.tempNode.nextPointer = self.head
            self.head = self.tempNode

    def __len__(self):  # This method calculates the list's length everytime when it is called. In order to avoid O(n) everytime and change it to O(1), we can cache the current count as an instance variable and update it on add/append/delete operations
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.nextPointer

        return count

    def returnCentreOfTheLinkedList(self):
        # If list has odd elements e.g. 5 elements, the pointer to 3rd element will be returned
        # If list has even element e.g. 4, the pointer to 2nd element will be returned
        if self.isHeadNone():
            return self.head
        slowPointer = fastPointer = self.head

        while fastPointer.nextPointer is not None and fastPointer.nextPointer.nextPointer is not None:
            slowPointer = slowPointer.nextPointer
            fastPointer = fastPointer.nextPointer.nextPointer

        return slowPointer



















