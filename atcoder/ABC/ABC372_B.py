def funcA(M):
    if M == 0:
        return [0]
    
    nums = []
    while M > 0:
        nums.append(M % 3)
        M //= 3
    
    return nums[::-1]

def output(M):
    base3 = funcA(M)
    N = sum(base3)
    A = []
    for i, digit in enumerate(base3):
        A.extend([len(base3) - 1 - i] * digit)
    return N, A

M = int(input())
N, A = output(M)

print(N)
print(*A)