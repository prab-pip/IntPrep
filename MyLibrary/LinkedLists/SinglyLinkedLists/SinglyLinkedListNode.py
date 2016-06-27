class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return '%s' %self.data

    def isNextNone(self):
        return self.next is None