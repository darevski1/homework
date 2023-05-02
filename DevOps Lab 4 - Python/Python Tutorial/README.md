## Python Tutorial

#### Python Comments

    #This is a comment
    print("Hello, World!")

### Data Types

    * Text Type: (str)
    * Numeric Types: (int, float, complex)
    * Sequence Types: (list, tuple, range)
    * Mapping Type: (dict)
    * Set Types: (set, frozenset)
    * Boolean Type: (bool - true/false)
    * Binary Type: (bytes, bytearray, memoryview)
    * None Type:  (NoneType)

## Casting

Whith casting we can specify data type of variable

     int()
     frloat()
     str()

## Python Lists

    myList = ["banana", "kiwi", "orange"]

Lists are used to store multiple items in a single variable, List items are ordered, changeable, and allow duplicate values.

    It is also possible to use the list() constructor when creating a new list.

### Access Items

    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])
    banana

### Change Item Value

    hislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)
    ['apple', 'blackcurrant', 'cherry']

### Append Items

    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)
    ['apple', 'banana', 'cherry', 'orange']

## Python Tuple

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and **_unchangeable_**

    thistuple = ("apple", "banana", "cherry")

## Python Dictionaries

Are used to store data and key:value pairs

    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
      }

Example output:

    print(thisdict)
     {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

## if else

    a = 200
    b = 33
    if b > a:
      print("b is greater than a")
    elif a == b:
      print("a and b are equal")
    else:
      print("a is greater than b")

## while loops

    i = 1
    while i < 6:
      print(i)
      i += 1

## For Loops

    list = ["one", "two", "three" ]
    for x in list
    	print(x)
