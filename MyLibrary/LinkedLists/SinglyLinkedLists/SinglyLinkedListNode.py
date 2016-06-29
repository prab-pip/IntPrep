class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.data = value
        self.nextPointer = None

    def __str__(self):
        return '%s' %self.data

    def isNextNone(self):
        return self.nextPointer is None