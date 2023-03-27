'''
1. Sort a list of dictionaries: Write a lambda function that sorts a list of dictionaries by a specified key.
For example, given the list of dictionaries 
[{ 'name': 'John', 'age': 25 }, { 'name': 'Alice', 'age': 30 }, { 'name': 'Bob', 'age': 20 }],
the lambda function should sort the list by age and return 
[{ 'name': 'Bob', 'age': 20 }, { 'name': 'John', 'age': 25 },{ 'name': 'Alice', 'age': 30 }].
'''
list = [{ 'name': 'John', 'age': 25 }, 
        { 'name': 'Alice', 'age': 30 }, 
        { 'name': 'Bob', 'age': 20 },
        { 'name': 'Ali', 'age': 18}
        ]
selected_key = 'age'

print("The list sorted by age: ")
print(sorted(list, key= lambda x: x[selected_key]))

###############################
'''
2. Calculate the average:
Write a lambda function that takes a list of numbers as input and returns the average value.
For example, given the list [1, 2, 3, 4, 5], the lambda function should return 3.
'''
from functools import reduce

input_list = [19, 452, 46, 82, 65, 101]
sum = reduce(lambda x,y: x+y, input_list)
ave = sum / len(input_list)

print('Avrage of input list= ', ave)

###############################
'''
3. Find the largest number:
Write a lambda function that takes a list of numbers as input and returns the largest number in the list.
For example, given the list [1, 5, 3, 9, 2], the lambda function should return 9.
'''
valuesList = [222,333,444,555,2,1]

print(max(valuesList, key= lambda value: int(value)) )
###############################
'''
4. Flatten a nested list:
Write a lambda function that takes a nested list as input and returns a flattened list.
For example, given the nested list [1, [2, [3, 4], 5], 6], the lambda function should return [1, 2, 3, 4, 5, 6]
'''
nestedlist = [[1, 2, 3], [3, 16, 17], [17, 5, 44],70]

flatten_list = lambda nestedlist:[element for item in nestedlist for element in flatten_list(item)] \
                                    if type(nestedlist) is list else [nestedlist]

print("Original list ", nestedlist)
print("Transformed List ", flatten_list(nestedlist))
###############################

'''
5. Calculate the median:
Write a lambda function that takes a list of numbers as input and returns the median value.
If the list has an even number of elements, the median should be the average of the middle two elements.
For example, given the list [1, 2, 3, 4, 5, 6], the lambda function should return 3.5.
'''
###############################
numbers = input('Input a list of numbers:')
int_number_list = list(map(lambda x: int(x), numbers.split(" ")))

index = len(int_number_list) / 2

a = (int_number_list[int(index)-1] + int_number_list[int(index)]) /2
b = int_number_list[int(index)]
middle = lambda a, b : a if index == int(index) else b

print('Middle= ', middle(a,b))



