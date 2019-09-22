def solution(a,b):
    if a>b : a,b = b,a
    return sum(list(range(a,b+1)))

print(solution(5,3))