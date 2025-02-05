# A
n, x = map(int,input().split())
numbers = list(map(int,input().split()))

for i in range(n):
  if numbers[i] == x:
    print(i + 1)
    exit()

# B
n = int(input())
opened_cards = []
marks = ("H","D","C","S")
numbers = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K")
for i in range(n):
  x = input()
  if x[0] not in marks:
    print("No")
    exit()
  if x[1] not in numbers:
    print("No")
    exit()
  if x in opened_cards:
    print("No")
    exit()
  opened_cards.append(x)

print("Yes")
