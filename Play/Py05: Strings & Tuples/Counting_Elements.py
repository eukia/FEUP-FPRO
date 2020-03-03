"""
Write a function count_until(tup) that, given a tuple tup, returns the number of elements in it before an element of the type tuple appears. If there isn’t a nested tuple, it should return -1.
Adapted from: w3resource > python-tuple-exercise-24 
"""
def count_until(tup):
    for i in tup:
        if type(i).__name__ == 'tuple':
            return tup.index(i)
    return -1
