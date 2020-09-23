print ('hello')
x = input("How old?")
print(x)

'''
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('hello')
hello
>>> x = input("How old?")
How old?23
>>> print(x)
23
>>> 
==================== RESTART: C:/Users/wrigh/src/midterm.py ====================
hello
How old?56
56
>>> name="Keith"
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str)

>>> help(name)
No Python documentation found for 'Keith'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help(name.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> name.lower()
'keith'
>>> name
'Keith'
>>> name = name.lower()
>>> name
'keith'
>>> name.capitalize()
'Keith'
>>> name
'keith'
>>> name = name.capitalize()
>>> name
'Keith'
>>> >>> help(name.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower
    case.
    
SyntaxError: invalid syntax
>>> date = "This is a good day to learn Python"
>>> data = date
>>> print(data)
This is a good day to learn Python
>>> print(data[0:3])
Thi
>>> print(data[0:4])
This
>>> print(data[0:-5])
This is a good day to learn P
>>> print(data[-1:-5])

>>> print(data[20:])
o learn Python
>>> print(data[:20])
This is a good day t
>>> print(data[-6:])
Python
>>> lang = data[-6:]
>>> print lang
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(lang)?
>>> print(lang)
Python
>>> colors=['red', 'blue', 'green', 'yellow']

>>> colors[0]
'red'
>>> colors[1]
'blue'
>>> colors[1:3]
['blue', 'green']
>>> favs = colors[1:3]
>>> favs
['blue', 'green']
>>> dir(colors)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> hue=('red', 'green', 'red', 'yellow')

>>> dir(hue)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> colors.sort()
>>> print(colors)
['blue', 'green', 'red', 'yellow']
>>> hue.sort()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    hue.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> help(hue.index)
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.tuple instance
    Return first index of value.
    
    Raises ValueError if the value is not present.

>>> hue.index('red')
0
>>> hue
('red', 'green', 'red', 'yellow')
>>> hue.count('red')
2
>>> hue.index('red',1)
2
>>> hue[0]
'red'
>>> hue[2]
'red'
>>> info={"name": "Bob Smith", "age": 25, "title": "manager"}

>>> dir(info)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> title = info['title']
>>> print (title)
manager
>>> print(info['age'])
25
>>> info.items()
dict_items([('name', 'Bob Smith'), ('age', 25), ('title', 'manager')])
>>> info.keys()
dict_keys(['name', 'age', 'title'])
>>> info.values()
dict_values(['Bob Smith', 25, 'manager'])
>>> name
'Keith'
>>> name == 'Bob'
False
>>> not name  == 'Bob'
True
>>> x = 3
>>> y = 3
>>> x == y or name == 'Bob'
True
>>> not x == y or name == 'Bob'
False
>>> not ( x == y or name == 'Bob')
False
>>> x = 4
>>> not ( x == y or name == 'Bob')
True
>>> x == y or name == 'Bob'
False
>>> not ( x == y or name == 'Bob')
True
>>> not x == y or name == 'Bob'
True
>>> pass
>>> help(pass)
SyntaxError: invalid syntax
>>>
'''
