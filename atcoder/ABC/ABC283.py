# A
a, b = map(int, input().split())

print(a ** b)

# B
n = int(input())
numbers = list(map(int,input().split()))
queries = int(input())

for i in range(queries):
  query = list(map(int,input().split()))
  if query[0] == 1:
    numbers[query[1]-1] = query[2]
  else:
    print(numbers[query[1]-1])