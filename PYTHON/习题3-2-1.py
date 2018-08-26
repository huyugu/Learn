"""
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
"""

def print_2(f):
    f()
    f()


def print_4(f):
    print_2(f)
    print_2(f)


def print_01():
    print("+ - - - - ", end="")


def print_02():
    print("+")


def print_03():
    print_4(print_01)
    print_02()


def print_04():
    print("|         ", end="")


def print_05():
    print("|")


def print_06():
    print_4(print_04)
    print_05()


def print_07():
    print_4(print_06)


def print_08():
    print_03()
    print_07()


def print_09():
    print_4(print_08)
    print_03()


print_09()
