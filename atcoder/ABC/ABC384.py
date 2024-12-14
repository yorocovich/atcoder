# A
n, b, a = input().split()
s = input()
ans = ""
for i in range(len(s)):
  if s[i] != b:
    ans += a
  else:
    ans += s[i]

print(ans)

# B
n, r = map(int,input().split())
ans = r
for i in range(n):
  d, a = map(int,input().split())
  if d == 1 and 1600 <= ans <= 2799:
    ans += a 
  elif d == 2 and 1200 <= ans <= 2399:
    ans += a
  
print(ans)

# C
def get_all_subsequences(s):
    result = []
    for i in range(1, 1 << len(s)):
        subsequence = ''
        for j in range(len(s)):
            if i & (1 << j):
                subsequence += s[j]
        if ''.join(sorted(subsequence)) == subsequence:
            result.append(subsequence)
    return result

def calculate_score(subsequence, scores):
    return sum(scores[ord(c) - ord('A')] for c in subsequence)

a, b, c, d, e = map(int, input().split())
scores = [a, b, c, d, e]

base_string = "ABCDE"
all_combinations = get_all_subsequences(base_string)

scored_combinations = []
for comb in all_combinations:
    score = calculate_score(comb, scores)
    scored_combinations.append((score, comb))

scored_combinations.sort(key=lambda x: (-x[0], x[1]))

for _, combination in scored_combinations:
    print(combination)