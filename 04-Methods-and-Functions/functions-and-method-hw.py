"""These are phyton problems to resolve"""
import string
from math import pi


# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    """FUNCTION: calculates the volume of the shape by radius
    PARAMETER: radius as a number
    RETURN: volume as a number"""
    return 4 / 3 * pi * rad ** 3


print(vol(1))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    """FUNCTION: Checks if the num is lower then high pram and num is higher than low param
    INPUTS: num=number we check, low=number the min+1 value, high=number max-1 value
     OUTPUT: True if the num is in the range of low and high"""
    return high > num > low


print(ran_check(2, 1, 3))
print(ran_check(1, 1, 3))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    """FUNCTION: prints the calculation of the lower and upper alphabetical character numbers
     INPUT: a string where we need to know how many upper and lower chars in
     OUTPUT: prints te measured values separately"""
    lower_counter = 0
    upper_counter = 0
    for char in s:
        if char.isalpha():
            if char.islower():
                lower_counter += 1
            else:
                upper_counter += 1

    print('No. of upper case characters: ' + str(upper_counter))
    print('No. of Lower case characters: ' + str(lower_counter))


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    """FUNCTION: one element can be only once in the list
    INPUT: list
    OUTPUT: set"""
    return set(lst)


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    """FUNCTION: multiplies the numbers in the list
    INPUT: a list where the elements should be multiplied
    OUTPUT: result of multiplication"""
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a passed in string is palindrome or not.
def palindrome(s):
    """FUNCTION: decide if the  input is palindrome
    INPUT: string what should be checked if that is palindrome
    OUTPUT: True if the input is palindrome"""
    rev = reverse(s)  # invoking reverse() method and assign that to the rev variable

    if s == rev:
        return True
    return False


def reverse(s):
    """FUNCTION: helper method that reverse the input string
    INPUT: a string
    OUTPUT: reversed input"""
    return s[::-1]


print(palindrome('helleh'))
print(palindrome('abc'))


# Write a Python function to check whether a string is pangram or not.
def ispangram(str1, alphabet=string.ascii_lowercase):
    """FUNCTION: checks if the input is pangram
    INPUT: str1 what should be checked, alphabet is already defined as a param so not necessary to redefine
    OUTPUT: True if the str1 contains all of the alphabetical letters"""
    for char in alphabet:
        if char not in str1:
            return False

    return True


print(ispangram('vmi'))
print(ispangram('The quick brown fox jumps over the lazy dog'))