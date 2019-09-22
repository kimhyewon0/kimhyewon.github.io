arr= [1,2,3]
def solution(arr):
    answer = []
    temp = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])

    answer.append(arr.pop())
    return answer

print(solution(arr))