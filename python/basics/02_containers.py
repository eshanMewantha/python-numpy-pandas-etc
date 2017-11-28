"""Lists"""
print('\nLists')
my_list = [3, 1, 5]                                 # Create a list
print('my_list      = ' + str(my_list))             # "[3, 1, 5]"
print('my_list[2]   = ' + str(my_list[2]))          # "5"
print('my_list[-1]  = ' + str(my_list[-1]))         # Negative indices count from the end of the list; prints "5"
print("my_list[2]   = 'foo'")
my_list[2] = 'foo'                                  # Lists can contain elements of different types
print('my_list      = ' + str(my_list))             # "[3, 1, 'foo']"
print("my_list.append('bar')")
my_list.append('bar')                               # Add a new element to the end of the list
print('my_list      = ' + str(my_list))             # "[3, 1, 'foo', 'bar']"
print("x = my_list.pop()")
x = my_list.pop()                                   # Remove and return the last element of the list
print('x = ' + str(x) + '   my_list = ' +str(my_list))    # "bar [3, 1, 'foo']"
