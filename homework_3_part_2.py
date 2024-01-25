def move_last_to_first(lst):

    if len(lst) <= 1:
        return lst

    last_element = lst.pop()
    lst.insert(0, last_element)

    return lst

# Example
print(move_last_to_first([12, 3, 4, 10]))
print(move_last_to_first([1]))
print(move_last_to_first([]))
print(move_last_to_first([12, 3, 4, 10, 8]))



# Creating a list
#lst = [1, 2, 3, 4, 5]
#
#if len(lst) > 1:
#    last = lst[-1]
#    lst.pop()
#    lst.insert(0, last)
#print(lst)
