# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print ( id (int_a), id (str_b), id (set_c), id (lst_d), id (dict_e), sep = '\n')


# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))


# 3. Define the type of each object from step 1
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e), sep ='\n')


# 4. Check the type of the objects by using isinstance.String formatting:
print(isinstance(int_a, int), isinstance(str_b, str), isinstance(set_c, set), isinstance(lst_d, list),
      isinstance(dict_e, dict), sep ='\n')


# 5. Replace the placeholders with a value:"Anna has ___ apples and ___ peaches.".
# With .format and curly braces {}
print('Anna has {0} apples and {1} peaches'. format(11, 7))


# 6. By passing index numbers into the curly braces.
print('Anna has {1} apples and {3} peaches'. format(2, 8, 6, 7))


# 7. By using keyword arguments into the curly braces.
print('Anna has {red} apples and {big} peaches'. format(red = 2, big = 7))


# 8. With indicators of field size (5 chars for the first and 3 for the second).
print('Anna has {0:0} apples and {2:0} peaches'. format(5, 4, 3))

# 9. With f-strings and variables.
red = "sour"
big = "sweet"
print(f'Anna has {red} apples and {big} peaches')


# 10. With % operator.
red = 5
big = 7
print('Anna has %s apples and %s peaches' %(red, big))


# 11. With variable substitutions by name (hint: by using dict)
# Comprehensions:
# (1)
#lst = []
#for num in range(10):
#      if num % 2 == 1:
#            lst.append(num ** 2)
#      else:
#             lst.append(num ** 4)
#print(lst)

# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]



# 12. Convert (1) to list comprehension.
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)


# 13 Convert (2) to to regular for with if-else.
list_comprehension = []
for num in range(10):
      if num % 2 == 0:
            list_comprehension.append(num // 2)
      else:
            list_comprehension.append(num * 10)
print(list_comprehension)


 # (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#           d[num] = num ** 2
# print(d)

# (4 )
#d = {}
#for num in range(1, 11):
#      if num % 2 == 1:
#            d[num] = num ** 2
#      else:
#            d[num] = num // 0.5
#print(d)
# (5) dict_comprehension = {x: x ** 3 для x в діапазоні (10), якщо x ** 3% 4 == 0}
# (6) dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}


# 14. Convert (3) to dict comprehension.
dict_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1 }
print(dict_comprehension)


# 15. Convert (4) to dict comprehension.
dict_comprehension = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension)


# 16. Convert (5) to regular for with if
d = {}
for x in range(10):
      if x ** 3 % 4 == 0:
            d[x] = x ** 3
print(d)


# 17. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
      if x ** 3 % 4 == 0:
            d[x] = x ** 3
      else:
            d[x] = x
print(d)


# Lambda:
# (7)
# def foo(x, y):
#      if x < y:
#            return x
#      else:
#            return y
#print(foo)

# (8)
# foo = lambda x, y, z: z if y < x and x > z else y


# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(4, 2))
# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x > z:
        return z
    else:
        return y
print(foo(2, 4, 5))


# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse = True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_new = list(map(lambda x: x * 2, lst_to_sort))
print(lst_new)

# 23*. Raise each list number to the corresponding number on another list:
# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(lambda x, y: x ** y, list_A, list_B))
print(list_C)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
sum = reduce(lambda a, b: a + b, lst_to_sort)
print(sum)


# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_list = list(filter(lambda x: (x % 2 == 1), lst_to_sort ))
print(new_list)

# 26. Considering the range of values:
# b = range(-10, 10), use the function filter to return only negative numbers.
old_list = range(-10, 10)
def foo(b):
    if b < 0:
        return b
    else:
        return False
new_list_1 = list(filter(foo, old_list))
print(new_list_1)


# 27*. Using the filter function, find the values that are common to the two lists:
# list_1 = [1,2,3,5,7,9]
# list_2 = [2,3,5,6,7,8]
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
new_list = list(filter(lambda x: x  in  list_1, list_2))
print(new_list)
