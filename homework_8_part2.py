def find_unique_value(some_list):
    count_dict = {}
    for x in some_list:
        if x in count_dict:
            count_dict[x] += 1
        else:
            count_dict[x] = 1
    for key, value in count_dict.items():
        if value == 1:
            return key
    return None
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")


#One more way of doing it!


def find_unique_value(some_list):
    unique_set = set()
    for x in some_list:
        if x not in unique_set:
            unique_set.add(x)
    if len(unique_set) == 1:
        return unique_set.pop()
    else:
        return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
