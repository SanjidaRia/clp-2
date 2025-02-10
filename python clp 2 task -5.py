import random
matrix = [[random.randint(1, 90) for _ in range(5)] for _ in range(5)]
RowSums = [sum(row) for row in matrix]
print("Matrix:")
for row in matrix:
    print(row)
print("\nRow-wise sums:")
print(RowSums)

