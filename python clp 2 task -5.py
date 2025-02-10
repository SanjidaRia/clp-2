import random
matrix = [[random.randint(1, 90) for _ in range(6)] for _ in range(6)]
RowSums = [sum(row) for row in matrix]
print("Matrix:")
for row in matrix:
    print(row)
print("\nRow-wise sums:")
print(RowSums)

