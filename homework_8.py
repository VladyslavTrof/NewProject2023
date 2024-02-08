def add_one(some_list):
    num_str = ''.join (str (digit) for digit in some_list)
    num_int = int (num_str) + 1
    result_str = str (num_int)
    result_list = list (int (digit) for digit in result_str)
    return result_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


# There is few different ways of doing this task.

def add_one(some_list):
    num_str = ''.join(str(digit) for digit in some_list)
    length = len(num_str)
    num_int = int(num_str) + 1
    result_str = str(num_int).zfill(length)
    result_list = list(int(digit) for digit in result_str)
    return result_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
