'''
1. Write a function that takes a list of integers as an argument, and returns the sum of the integers. 
Use a try-except block to catch any ValueError exceptions that may be raised when attempting 
to convert a string to an integer.
'''
def My_sum(int_list):
    sum = 0
    if len(int_list) > 1:
        try:
            for each_number in int_list:
                sum += int(each_number)     
        except ValueError:
            print('Only a list of alphabetic characters are acceptable.')
            return(False)
        else:
            return(sum)
    else:
        return int_list[0]    
aa = [1,2,3,4]
bb = ['1','2','3','4']
print ( 'Sum of arguments is: ', My_sum(bb))

'''
2. Write a function that takes a filename as an argument, and attempts to open the file. 
Use a try-except block to catch any FileNotFoundError exceptions that may be raised when attempting to open the file. 
If the file is successfully opened, the function should return the contents of the file.
'''
def Open_file(inp_filename):
    try:
        with open(inp_filename, 'r') as myfile:
            file_content = myfile.readlines()
        return file_content
    except FileNotFoundError:
        print('Filename does not exist.')
        return(False)
    except Exception as e:
        print('Error is: ', e)

#print(Open_file('C:/Python/class/class1.docx'))

'''
3. Write a function that takes a list of strings as an argument, and returns a new list containing only the strings
that can be successfully converted to a float. Use a try-except block to catch any ValueError exceptions 
that may be raised when attempting to convert a string to a float.
'''
def only_floats(input_list):
    result = []
    
    for item in input_list:
        try:   
            b = float(item)
            result.append(b)
        except ValueError:
            continue
    print('List of only float numbers: ', result) 

only_floats(['21', '66.6a', '65', '49.5', 'ss', 'f454'])
'''
4. Write a function that takes a list of dictionaries as an argument, and returns the value of a specified key 
from each dictionary. Use a try-except block to catch any KeyError exceptions that may be raised when attempting to 
access a key that does not exist in a dictionary.
'''
def valu_of_key(input_list_of_dic, the_key):
    result =[]
    for item in input_list_of_dic:
        try:
            result.append(item[the_key])
        except KeyError:
            continue
    print('Values of all-', the_key, '-Keys are: ', result)

my_list = [{'student':'Ali',        'grade':'17'}, 
            {'student':'Hasan',     'grade':'19.2'}, 
            {'student':'Reza',      'grade':'19.8'},
            {'student':'Ashkan',    'filal':'17.3'}
            ]
valu_of_key(my_list, 'grade')
'''
5. Write a function that takes a list of integers as an argument, and returns the largest integer in the list. 
Use a try-except block to catch any ValueError exceptions that may be raised when attempting to compare elements 
that are not integers.
'''
def Largest_int(input_list_of_int):
    
        biggest = int(input_list_of_int[0])
        for item in input_list_of_int:
            try:
                if int(item) > biggest:
                    biggest = item
            except ValueError:
                continue
        print('The largest integer of ', input_list_of_int, 'is: ', biggest) 

a = [22, 643, 69, 2435, -223]
b = [22, 643, 'ws', 2435, -223]
Largest_int(b)