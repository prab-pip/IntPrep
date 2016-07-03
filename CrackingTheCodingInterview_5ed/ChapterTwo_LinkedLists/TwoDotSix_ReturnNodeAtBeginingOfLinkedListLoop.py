class Solution(object):
    def __init__(self, linkedListObject):
        self.linkedListObject = linkedListObject

    def returnNodeAtBeginingOfLinkedListLoop(self):
        if not self.linkedListObject.isHeadNone():
            slowPointer = self.linkedListObject.head.nextPointer

            if slowPointer is not None:
                fastPointer = slowPointer.nextPointer
            else:
                print 'No loop in the Linked List here as well'
                return
        else:
            print 'No loop in the Linked List here'
            return

        while slowPointer is not None and fastPointer is not None and fastPointer.nextPointer is not None and slowPointer != fastPointer:
            slowPointer = slowPointer.nextPointer
            fastPointer = fastPointer.nextPointer.nextPointer

        if slowPointer is None or fastPointer is None or fastPointer.nextPointer is None:
            print 'There is no loop in the Linked List'
            return
        collisionPoint = slowPointer

        slowPointer = self.linkedListObject.head

        while slowPointer != fastPointer:
            slowPointer = slowPointer.nextPointer
            fastPointer = fastPointer.nextPointer

        return slowPointer, collisionPoint
