
import string

import keyword

def is_valid_variable_name(name):

    if not name:
        return False

    if name[0].isdigit():
        return False

    if name.isdigit():
        return False

    if any(c.isupper() or c.isspace() or c in string.punctuation and c != "_" for c in name):
        return False

    if name in keyword.kwlist:
        return False

    return True

print(is_valid_variable_name("_"))
print(is_valid_variable_name("x"))
print(is_valid_variable_name("get_value"))
print(is_valid_variable_name("get value"))
print(is_valid_variable_name("get!value"))
print(is_valid_variable_name("some_super_puper_value"))
print(is_valid_variable_name("Get_value"))
print(is_valid_variable_name("get_Value"))
print(is_valid_variable_name("getValue"))
print(is_valid_variable_name("3m"))
print(is_valid_variable_name("m3"))
#vlad test one to be done on this file 