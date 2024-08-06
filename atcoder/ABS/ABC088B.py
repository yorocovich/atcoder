n = input()
card_numbers = list(map(int, input().split()))
alice_points = 0
bob_points = 0

sorted_card_numbers = sorted(card_numbers, reverse=True)

i = 0
for number in sorted_card_numbers:
  if i % 2 == 0:
    alice_points += number
  else:
    bob_points += number
  i += 1

print(alice_points - bob_points)
