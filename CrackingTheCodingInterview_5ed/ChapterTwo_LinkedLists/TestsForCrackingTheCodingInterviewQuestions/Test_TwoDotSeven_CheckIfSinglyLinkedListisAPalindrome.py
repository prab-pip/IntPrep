import unittest

from MyLibrary.LinkedLists.SinglyLinkedLists.SinglyLinkedList import SinglyLinkedList
from CrackingTheCodingInterview_5ed.ChapterTwo_LinkedLists.TwoDotSeven_CheckIfSinglyLinkedListisAPalindrome import Solution

class Test_CheckIfSinglyLinkedListisAPalindrome_method1(unittest.TestCase):
    def test_empty_list(self):
        singlyLinkedList = SinglyLinkedList()

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_one_value(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_two_values_not_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = False  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


    def test_list_with_two_values_is_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_three_values_not_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 3]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = False  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


    def test_list_with_three_values_is_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_four_values_not_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 1, 2]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = False  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


    def test_list_with_four_values_is_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 2, 1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


class Test_CheckIfSinglyLinkedListisAPalindrome_method2(unittest.TestCase):
    def test_empty_list(self):
        singlyLinkedList = SinglyLinkedList()

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_one_value(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_two_values_not_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = False  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


    def test_list_with_two_values_is_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method1()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_three_values_not_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 3]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = False  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


    def test_list_with_three_values_is_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_four_values_not_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 1, 2]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = False  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


    def test_list_with_four_values_is_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 2, 1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))

    def test_list_with_five_values_not_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 3, 2, 4]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = False  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))


    def test_list_with_five_values_is_a_palindrome(self):
        singlyLinkedList = SinglyLinkedList()

        inputList = [1, 2, 3, 2, 1]
        singlyLinkedList.populate(inputList)

        s = Solution(singlyLinkedList)

        expectedValue = True  # Considering empty list is a palindrome
        receivedValue = s.method2()
        self.assertTrue(expectedValue == receivedValue, "Expected: %s, Received: %s" %(expectedValue, receivedValue))