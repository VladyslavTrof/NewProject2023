#Input: [[1,2],[3,4],[5,6]]
#Output: [[1,3,5],[2,4,6]]
#Explanation: Suppose we are given a matrix
#                       [[1, 2],
#                        [3, 4],
#                        [5, 6]]
#Then the transpose of the given matrix will be,
#                      [[1, 3, 5],
#                        [2, 4, 6]]

# Python3 code to demonstrate
# matrix creation of n * n
# using list comprehension

# initializing N
N = 4

# printing dimension
print("The dimension : " + str(N))

# using list comprehension
# matrix creation of n * n
res = [list(range(1 + N * i, 1 + N * (i + 1)))
							for i in range(N)]

# print result
print("The created matrix of N * N: " + str(res))
