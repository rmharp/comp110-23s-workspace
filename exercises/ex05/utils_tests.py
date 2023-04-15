from exercises.ex05.utils import only_evens, sub, concat
"""Unit Test Functions."""

__author__: """730470865"""

def unit_only_evens():
    assert(only_evens([1,2,3,4]) == [2,4])

def unit_only_evens_empty():
    assert(only_evens([]) == [])

def unit_concat():
    assert(concat([1,2],[3,4]) == [1,2,3,4])

def unit_concat_empty():
    assert(concat([],[]) == [])

def unit_sub():
    assert(sub([1,2,3,4,5],1,3) == [2,3])

def unit_sub_empty():
    assert(sub([],1,3) == [2,3])

