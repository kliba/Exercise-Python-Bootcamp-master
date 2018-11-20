"""The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
syntax:
for val in sequence:
	Body of for"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# simple examples of for loop
for num in my_list:
    print(num)

for num in my_list:
    print('Hello')

# sum the my_list elements using for loop
sum = 0

for num in my_list:
    sum += num

print(sum)

## let's print a string chars
word = "something for this string"

for char in word:
    print(char)

# list of tulpes
list_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]

for tup in list_of_tuples:   # prints trouble pairs
    print(tup)

for (a, b) in list_of_tuples: # prints tuples elements
    print(a)
    print(b)

# iterate on a dictionary
d = {'k1':1, 'k2':2, 'k3':3}

for key, values in d.items():  # prints only the keys
    print(key)