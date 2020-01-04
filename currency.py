"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Nicholas Johnston
Date:   January 3rd 2020
"""

import introcs

APIKEY = "8mNy0uxE2kaogoJoprIscPANUb8YWurAFq0Y84q9oLIe"


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert introcs.find_str(s, ' ') >= 0
    space_index = introcs.index_str(s, ' ')
    split_string = s[:space_index]
    return split_string


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: before_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert introcs.find_str(s, ' ') >= 0
    space_index = introcs.index_str(s, ' ')
    split_string = s[space_index+1:]
    return split_string


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    first_quote = introcs.find_str(s, '"')
    second_quote = introcs.find_str(s, '"', first_quote+1)
    result = s[first_quote+1:second_quote]
    return result
