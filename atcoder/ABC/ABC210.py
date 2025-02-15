n, a, x, y = map(int,input().split())
ans = n * x if n <= a else a * x + (n - a) * y
print(ans)