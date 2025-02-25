def f(k: int) -> int:
  if k == 0 or k == 1:
    return 1
  return k * f(k - 1)

x = int(input())

print(f(x))