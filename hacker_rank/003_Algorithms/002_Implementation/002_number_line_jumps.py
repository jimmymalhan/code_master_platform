# Kangaroo 1 starts at x1 = 2 with a jump distance v1 = 1
# and kangroo 2 starts at x2 = 1 with a jump distance v2 = 2
# after one jump, they  are both ar x = 3,
# (x1 + v1 = 2 + 1, x2 + v2 = 1 + 2)
# so our answer is YES

def kangaroo(x1, v1, x2, v2):
    return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'

x1, v1, x2, v2 = map(int, input().split())
print(kangaroo(x1, v1, x2, v2))