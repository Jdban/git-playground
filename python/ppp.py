# from typing import Dict
import sys
import re


def method(self,
           lst,  # type: List[str]
           opt=0,  # type: int
           *args,  # type: str
           **kwargs  # type: bool
           ):

def method2(self, lst, opt=0, *args, **kwargs):  # type: (List[str], int, str, bool) -> int
    asd


# type: (...) -> int

def my_func(numz, strz):  # type: (int, str) -> None
    numz *= 5
    # strz += "str"


class j_class:

    def __init__(self):
        self.apple = "hello"  # type: str

    @staticmethod
    def some_method(some_num):  # type: (int) -> str
        ret = some_num == 4
        return -1

print "hello world"

stra = "5"

num = 2

# result = stra + num

# my_list = []  # type: List[int]
#
# my_list.append(5)
#
# my_list.append("2")

my_func(5, "10")

# my_func("5", 10)

# some_num = 5 * my_func(5, "5")


some_map = {}  # type: Dict[str, int]

some_map[5] = 50

some_map["5"] = 54

print some_map[5]
print some_map.get("5")
print some_map.get(5)
print some_map["5"]


thing = j_class()  # type: j_class

print thing.some_method(2)


