
a = ['zzz','car','zza','sit']
n=1
def solution(a, n):
    answer =[]
    b = tuple(enumerate(a))
    b = sorted(sorted(b), key=lambda x: x[n])
    for i in b:
        answer. append(i[1])
    return answer
print(solution(a,n))