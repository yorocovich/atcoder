# A
a, b = map(int,input().split())

print(a ** b + b ** a)

# B
def is_palindrome(s: str) -> bool:
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

s = input()
ans = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        substr = s[i:j+1]
        if is_palindrome(substr):
            ans = max(ans, len(substr))

print(ans)