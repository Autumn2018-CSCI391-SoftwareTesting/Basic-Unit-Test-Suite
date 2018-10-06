import unittest
import shunting_yard as sy


class TokenizeTest(unittest.TestCase):
    def test_single_operator(self):
        tokens = list(sy.tokenize('1+2'))
        self.assertListEqual(tokens, ['1', '+', '2'])

    def test_multiple_operators(self):
        tokens = list(sy.tokenize('1+2-3'))
        self.assertListEqual(tokens, ['1', '+', '2', '-', '3'])

'''
IsOperatorTest tests the helper function 'isOperator(arg1)' in shunting_yard.py.
'isOperator(arg1)' should return true when testing the following math operators:
(plus [+], minus [-], multiplication [*], and division operators [/]).
-------------------------------------------------------------------------------------
:param: single string-character mathematics operator accepted.
'''
class IsOperatorTest(unittest.TestCase):
    #Pass an operator
    def test_an_operator(self):
        isOperator = sy.isOperator('-')
        self.assertTrue(isOperator)

    #Pass a numeric character
    def test_non_operator(self):
        isOperator = sy.isOperator('0')
        self.assertFalse(isOperator)

    #Pass a string
    def test_a_string(self):
        with self.assertRaises(ValueError):
            sy.isOperator('21')

    #Pass an empty string
    def test_empty_char(self):
        with self.assertRaises(ValueError):
            sy.isOperator('')

    #Pass an integer type
    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            sy.isOperator(1)

'''
IsDigitTest tests the helper function 'isDigit(arg1)' in shunting_yard.py.
'isDigit(arg1)' should return true when testing for single-digit numeric characters.
-------------------------------------------------------------------------------------
:param: single string-character digit accepted.
'''
class IsDigitTest(unittest.TestCase):

    #Pass a single digit character.
    def test_single_digit(self):
        isDigit = sy.isDigit('0')
        self.assertTrue(isDigit)

    #Pass a multiple-digit character.
    def test_large_digit(self):
        with self.assertRaises(ValueError):
            sy.isDigit('666')

    #Pass a non-digit
    def test_non_digit(self):
        sy.isDigit('a')
        self.assertRaises(Exception)

    #Pass an empty char
    def test_empty_char(self):
        with self.assertRaises(ValueError):
            sy.isDigit('')

    #Pass an integer type
    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            sy.isDigit(1)

'''
IsLeftBracketTest tests the helper function 'isLeftBracket(arg1)' in shunting_yard.py.
'isLeftBracket(arg1)' should return true when testing for a single opening-bracket.
Accepted opening brackets are: (left parenthesis [(], left square bracket [[])
-------------------------------------------------------------------------------------
:param: single character opening-bracket or opening-parenthesis accepted.
'''
class IsLeftBracketTest(unittest.TestCase):

    #Pass a single opening bracket
    def test_single_left_bracket(self):
        self.assertTrue(sy.isLeftBracket('['))

    #Pass a single closing parenthesis
    def test_single_right_parenthesis(self):
        self.assertFalse(sy.isLeftBracket(']'))

    #Pass a single closing bracket
    def test_single_right_bracket(self):
        self.assertFalse(sy.isLeftBracket(')'))

    #Pass multiple opening brackets
    def test_multiple_left_brackets(self):
        with self.assertRaises(ValueError):
            sy.isLeftBracket('[(')

    #Pass a non-opening bracket
    def test_non_left_bracket(self):
        self.assertFalse(sy.isLeftBracket('a'))

    #Pass an empty char
    def test_empty_char(self):
        with self.assertRaises(ValueError):
            sy.isLeftBracket('')

    #Pass an integer type
    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            sy.isLeftBracket(1)

'''
IsRightBracketTest tests the helper function 'isRightBracket(arg1)' in shunting_yard.py.
'isRightBracket(arg1)' should return true when testing for a single closing-bracket.
Accepted closing brackets are: (right parenthesis [)], right square bracket []])
-------------------------------------------------------------------------------------
:param: single character closing-bracket or closing-parenthesis accepted.
'''
class IsRightBracketTest(unittest.TestCase):

    #Pass a single closing bracket
    def test_single_right_bracket(self):
        self.assertTrue(sy.isRightBracket(']'))

    #Pass a single opening parenthesis
    def test_single_left_parenthesis(self):
        self.assertFalse(sy.isRightBracket('('))

    #Pass a single opening bracket
    def test_single_left_bracket(self):
        self.assertFalse(sy.isRightBracket('['))

    #Pass multiple closing brackets
    def test_multiple_right_brackets(self):
        with self.assertRaises(ValueError):
            sy.isRightBracket(')]')

    #Pass a non-closing bracket
    def test_non_left_bracket(self):
        self.assertFalse(sy.isRightBracket('a'))

    #Pass an empty char
    def test_empty_char(self):
        with self.assertRaises(ValueError):
            sy.isRightBracket('')

    #Pass an integer type
    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            sy.isRightBracket(1)

'''
IsNumberTest tests the helper function 'isNumber(arg1)' in shunting_yard.py.
'isNumber(arg1)' should return true if passed arguments are valid integer numbers.
-------------------------------------------------------------------------------------
:param: single or multi-digit numbers string-characters accepted
'''

class IsNumberTest(unittest.TestCase):
    #Pass a single digit
    def test_single_digit(self):
        self.assertTrue(sy.isNumber('0'))

    #Pass a large number
    def test_large_digit(self):
        self.assertTrue(sy.isNumber('420'))

    #Pass a non-digit
    def test_non_digit(self):
        self.assertFalse(sy.isNumber('A113'))

    #Pass an empty char
    def test_empty_char(self):
         with self.assertRaises(ValueError):
             sy.isNumber('')

    #Pass an integer type
    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            sy.isNumber(1)

'''
PeekAtStackTest tests the helper function 'peekAtStack(arg1)' in shunting_yard.py.
'peekAtStack(arg1)' should return a copy of the top-most (most recently added) item
from the given stack, arg1.
-------------------------------------------------------------------------------------
:param: python list
'''

class PeekAtStackTest(unittest.TestCase):

    #Get the most recently added item from a stack containing already three items.
    def test_get_from_non_empty_stack(self):
       testStack = []
       testStack.insert(0, 'WALL-E')
       testStack.insert(0, '2001: A Space Odyssey')
       testStack.insert(0, 'Monsters Inc.')
       mostRecentItem = sy.peekAtStack(testStack)
       self.assertEqual(mostRecentItem, 'Monsters Inc.', 'Top-most item not copied from stack')

    #Get the most recently added item from an empty stack.
    def test_get_from_empty_stack(self):
        testStack = []
        with self.assertRaises(IndexError):
            sy.peekAtStack(testStack)

    #Send a wrong type into the arguments.
    def test_pass_wrong_arg(self):
        with self.assertRaises(TypeError):
            sy.peekAtStack('Hello, world!')


'''
PopFromStackTest tests the helper function 'popFromStack(arg1)' in shunting_yard.py.
'popFromStack(arg1)' should remove and return the top-most (most recently added) item
from the given stack, arg1.
-------------------------------------------------------------------------------------
:param: python list
'''

class PopFromStackTest(unittest.TestCase):

    #Pop the most recently added item from a stack containing already three items.
    def test_pop_from_non_empty_stack(self):
        testStack = []
        testStack.insert(0, 'Things you should know for the exam: ')
        testStack.insert(0, 'Everything')
        testStack.insert(0, 'Everything + 1')
        self.assertEqual(sy.popFromStack(testStack), 'Everything + 1', 'Top-most item not copied from stack')
        self.assertEqual(len(testStack), 2, 'Top-most item not popped (removed) from stack')

    #Pop from an empty stack
    def test_pop_from_empty_stack(self):
        testStack = []
        with self.assertRaises(IndexError):
            sy.popFromStack(testStack)

    #Send wrong type into arguments
    def test_pass_wrong_arg(self):
        with self.assertRaises(TypeError):
            sy.peekAtStack('Hello, World')


'''
PushToStackTest tests the helper function 'pushToStack(arg1, arg2)' in shunting_yard.py.
'pushToStack(arg1, arg2)' should add an item to the top of the stack
-------------------------------------------------------------------------------------
:param: python list
'''


class PushToStackTest(unittest.TestCase):

    #Push (add) an item to an empty stack
    def test_push_to_empty_stack(self):
        testStack = []
        sy.pushToStack(testStack, 'Quotes')
        self.assertEqual(len(testStack), 1, 'Stack does not contain 1 item.')

    #Push (add) an item to a non-empty stack
    def test_push_to_non_empty_stack(self):
        testStack = ['Minas Tirith', 'Minas Ithil', 'Barad-dûr']
        sy.pushToStack(testStack, 'Isengard')
        self.assertEqual(len(testStack), 4, 'Stack does not contain 4 items')
        self.assertEqual(testStack[0], 'Isengard')
        self.assertEqual(testStack[1], 'Minas Tirith')

    #Pass wrong argument types
    def test_pass_wrong_arg(self):
        with self.assertRaises(AttributeError):
            sy.pushToStack(0, 'World')


'''
StackIsEmptyTest tests the helper function 'stackIsEmpty(arg1)' in shunting_yard.py
'stackIsEmpty(arg1)' should return true if the stack is empty, and false otherwise.
-------------------------------------------------------------------------------------
:param: python list
'''

class StackIsEmptyTest(unittest.TestCase):

    #Test an empty stack
    def test_empty_stack(self):
        testStack = []
        self.assertTrue(sy.stackIsEmpty(testStack))

    #Test non-empty stack
    def test_non_empty_stack(self):
        testStack = ['definently not empty']
        self.assertFalse(sy.stackIsEmpty(testStack))

    #Send wrong types into arguments
    def test_pass_wrong_arg(self):
        testStack = []
        with self.assertRaises(TypeError):
            sy.stackIsEmpty()
        with self.assertRaises(TypeError):
            sy.stackIsEmpty('')