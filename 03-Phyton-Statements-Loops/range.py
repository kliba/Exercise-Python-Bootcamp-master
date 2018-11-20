"""In a nutshell, it generates a list of numbers, which is generally used to iterate over with for loops.
There's many use cases. Often you will want to use this when you want to perform an action X number of times,
where you may or may not care about the index. Other times you may want to iterate over a list
(or another iterable object), while being able to have the index available.
The range() function works a little bit differently between Python 2.x and 3.x under the hood,
however the concept is the same. We'll get to that a bit later, however.
range([start], stop[, step])"""

# simple example using range
for num in range(0, 10):
    print(num)

# using the step param
for num in range(0, 10, 2):
    print(num)

# using enumerate keyword
word = 'abcde'

for item in enumerate(word):
    print(item)     # prints tuples key is index and value is  item

# using zip

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(zip(list1, list2))    # here it prints only the memory address of this zip

for item in zip(list1, list2):
    print(item)             # prints tuples