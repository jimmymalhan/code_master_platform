import os
S = os.listdir(os.getcwd())

def solution(S):
    # S = os.listdir(os.getcwd())
    S.sort(key=lambda f: os.stat(f).st_size, reverse=True)
    S.sort(key=lambda a: os.stat(a).st_atime, reverse=True)
    return S

print(solution(S))