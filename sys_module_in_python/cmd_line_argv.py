import sys

n = len(sys.argv)
print("Total no of arguments: ", n)

print("\nName of the Python script: ", sys.argv[0])

print("Other arguments", end=" ")
for i in range(1,n):
    print(sys.argv[i], end=" ")

Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])
print(f"\n\n{Sum}")