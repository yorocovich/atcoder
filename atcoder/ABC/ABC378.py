# A
balls = list(map(int,input().split()))

x = []
ans = 0
for ball in balls:
  if ball in x:
    x.remove(ball)
    ans += 1
  else:
    x.append(ball)

print(ans)

# B
N = int(input())
garbage = []
for i in range(N):
    qi, ri = map(int, input().split())
    garbage.append((i+1, qi, ri))

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    _, q, r = garbage[t-1]
    
    if d < r:
        print(r)
    else:
        n = (d - r) // q
        if (d - r) % q == 0:
            print(r + q * n)
        else:
            print(r + q * (n + 1))

# C
def find_previous_occurrences(N, A):
    last_seen = {}
    B = []
    
    for i in range(N):
        current = A[i]
        if current in last_seen:
            B.append(last_seen[current] + 1)
        else:
            B.append(-1)
        last_seen[current] = i
    
    return B

N = int(input())
A = list(map(int, input().split()))
result = find_previous_occurrences(N, A)
print(*result)