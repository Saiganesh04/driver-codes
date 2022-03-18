import math
def solve(n: int) -> str:
    n = int(n)
    ls = []
    while n % 2 == 0:
        ls.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            ls.append(i)
            n = n / i

    if n > 2:
        ls.append(n)
       
    s = set(ls)
    if len(s)>2:
        return 'Regular'
       
    else:
        if len(s)==1:
            if 2 in s or 7 in s:
                return 'Special'
            else:
                return 'Regular'
        else:
            if 2 in s:
                if 7 in s:
                    return 'Special'
            elif 7 in s:
                if 2 in s:
                    return 'Special'
            else:
                return 'Regular'

    return 'Regular'
T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
