import math
a = [93,30,55]
b= [1,30,5]

def solution(progresses, speeds):
    answer = []
    pro = []
    front = 0
    # 남은 작업의 퍼센트 구하고 speeds로 나누기
    pro = [math.ceil((100 - i)/j) for i,j in zip(progresses,speeds)]

    for idx in range(1,len(pro)):
        if pro[front] < pro[idx]:
            answer.append(idx - front)
            front = idx
    answer.append(len(pro)-front)
    return answer

