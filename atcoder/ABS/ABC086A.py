# input space separate
a, b = map(int, input().split())

# output
print("Odd" if (a * b) % 2 == 1 else "Even")
