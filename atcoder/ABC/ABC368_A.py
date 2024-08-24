n, k = map(int,input().split())
cards = [int(_) for _ in input().split()]

pos = k * -1
last_cards = cards[pos:]
cards = cards[:pos]
cards = last_cards + cards

print(' '.join(map(str, cards))) 
