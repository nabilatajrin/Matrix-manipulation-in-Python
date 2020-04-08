import numpy as np

result = np.dot(3, 7)
print("Dot product : ", result)

result = np.dot(9, 8)
print("Dot product : ", result)

# alternative
def np_dot(x, y):
    z = x * y
    return z

result2 = np_dot(3, 7)
print(result2)
result2 = np_dot(9, 8)
print(result2)

vector_a = np.array([[1, 4], [5, 6]])
vector_b = np.array([[2, 4], [5, 2]])
result2 = np_dot(vector_a, vector_b)
print(result2)