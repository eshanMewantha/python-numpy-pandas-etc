"""Reference http://cs231n.github.io/python-numpy-tutorial/#python-basic"""

"""
integer
"""
print("\nInteger")
x = 5
y = 4
print('x       = ' + str(x))          # x; prints "5"
print('y       = ' + str(y))          # y; prints "4"
print('x type  = ' + str(type(x)))    # type; prints "<class 'int'>"
print('y type  = ' + str(type(y)))    # type; prints "<class 'int'>"
print('x + y   = ' + str(x + y))      # Addition; prints "9"
print('x - y   = ' + str(x - y))      # Subtraction; prints "1"
print('x * y   = ' + str(x * y))      # Multiplication; prints "20"
print('x / y   = ' + str(x / y))      # Division; prints "1.25"  Returns a float
print('x ** y  = ' + str(x **y))      # Exponentiation; prints "625"
x += 1                                # Addition Assignment prints "6"
print('x += 1 ==> x = ' + str(x))
x = 5
x *= 2                                # Multiplication Assignment prints "10"
print('x *= 1 ==> x = ' + str(x))

print("\nFloat")
x = 5.2
y = 4.1
print('x       = ' + str(x))          # x; prints "5"
print('y       = ' + str(y))          # y; prints "4"
print('x type  = ' + str(type(x)))    # type; prints "<class 'float'>"
print('y type  = ' + str(type(y)))    # type; prints "<class 'float'>"
print('x + y   = ' + str(x + y))      # Addition; prints "9.3"
print('x - y   = ' + str(x - y))      # Subtraction; prints "1.1000000000000005"
print('x * y   = ' + str(x * y))      # Multiplication; prints "21.32"
print('x / y   = ' + str(x / y))      # Division; prints "1.2682926829268295"
print('x ** y  = ' + str(x **y))      # Exponentiation; prints "862.2112971316182"
x += 1                                # Addition Assignment prints "6.4"
print('x += 1 ==> x = ' + str(x))
x = 5.2
x *= 2                                # Multiplication Assignment prints "10.4"
print('x *= 1 ==> x = ' + str(x))

print("\nBoolean")
t = True
f = False
print('t       = ' + str(t))          # t; prints "True"
print('f       = ' + str(f))          # f; prints "False"
print('t type  = ' + str(type(t)))    # type; prints "<class 'bool'>"
print('f type  = ' + str(type(f)))    # type; prints "<class 'bool'>"
print('t AND f = ' + str(t and f))    # Logical AND; prints "False"
print('t OR f  = ' + str(t or f))     # Logical OR; prints "True"
print('NOT t   = ' + str(not t))      # Logical NOT t; prints "False"
print('NOT f   = ' + str(not f))      # Logical NOT f; prints "True"
print('t XOR f = ' + str(t != f))     # Logical t XOR f; prints "True"

print('\nString')
x = 'hello'                           # String literals with single quotes
y = "world"                           # String literals with single quotes
print('x       = ' + x)               # x; prints "hello"
print('y       = ' + y)               # x; prints "hello"
print('x length= ' + str(len(x)))     # String length; prints "5"
hw = x + ' ' + y                      # String concatenation
print('x + y   = ' + hw)              # prints "hello world"
hw12 = '%s %s %d' % (x, y, 12)        # sprintf style string formatting
print('%s %s %d % (x, y, 12) ==> ' + hw12)  # prints "hello world 12"

s = x
print('s.capitalize() = ' + s.capitalize())              # Capitalize a string; prints "Hello"
print('s.upper()      = ' + s.upper())                   # Convert a string to uppercase; prints "HELLO"
print('s.lower()      = ' + s.lower())                   # Convert a string to lowercase; prints "hello"
print('s.rjust(7)     = ' + s.rjust(7))                  # Right-justify a string, padding with spaces; prints "  hello"
print('s.center(7)    = ' + s.center(7))                 # Center a string, padding with spaces; prints " hello "
print('s.replace(l, (ell)) = ' + s.replace('l', '(ell)'))# Replace all instances of one substring with another;
                                                         # prints "he(ell)(ell)o"
print('  world .strip()    = ' + '  world '.strip())     # Strip leading and trailing whitespace; prints "world"
