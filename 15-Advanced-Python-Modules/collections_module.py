"""Collections Module
The collections module is a built-in module that implements specialized container data types providing alternatives to
Python’s general purpose built-in containers. We've already gone over the basics: dict, list, set, and tuple.

Now we'll learn about the alternatives that the collections module provides.
"""

# Counter
# Counter is a dict subclass which helps count hashable objects. Inside of it elements are stored as
# dictionary keys and the counts of the objects are stored as the value.
from collections import Counter

lst = [1, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1, 4, 3, 4, 4, 3, 234, 432, 432, 423, 101]
print(Counter(lst))
