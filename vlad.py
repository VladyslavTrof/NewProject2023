


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

# My simplified code
import re

def is_valid_variable_name(name):
    # Use a regular expression to check if the name matches the rules
    return bool(re.match(r"^[a-z_]\w*$", name) and name not in keyword.kwlist)
