A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("test 01: A =", A)
print("test 02: A[1] =", A[1])      # 2nd row
print("test 03: A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("test 04: A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])

print("test 05: 3rd column =", column)