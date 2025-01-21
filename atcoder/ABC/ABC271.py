hex_code = ["A","B","C","D","E","F"]

n = int(input())
a = n // 16
b = n % 16
ans = ""

#255なので2桁まで
if a > 9:
  ans += hex_code[a % 16 - 10]
else:
  ans += str(a % 16)

if b > 9:
  ans += hex_code[b % 16 - 10]
else:
  ans += str(b % 16)

print(ans)