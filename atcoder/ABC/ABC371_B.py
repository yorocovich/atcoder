def is_taro(N, children):
    first_male = [False] * N
    results = []

    for house, gender in children:
        house_index = house - 1 
        if gender == 'M' and not first_male[house_index]:
            first_male[house_index] = True
            results.append("Yes")
        else:
            results.append("No")

    return results

N, M = map(int, input().split())
children = [input().split() for _ in range(M)]

children = [(int(house), gender) for house, gender in children]

results = is_taro(N, children)

for result in results:
    print(result)