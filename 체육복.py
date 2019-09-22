n = 7
lost =[2,3,4]
reserve = [1,2,3,6]

#n = 전체학생수
#lost = 잃어버린학생들
#reserve 여분을 가지고 있는 학생들
def solution(n, lost, reserve):
    temp= []
    answer = n-len(lost)
    #중복되는 값이 있으면 reserve에서 제거하고 answer 추가
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            temp.append(i)
            answer +=1

    #reserve에 남은 값이 있다면
    #lost[i]-1 혹은 lost [i]+1이 reserve 안에 있다면 +=1
    for i in lost:
        if i in temp:
            continue
        if len(reserve) == 0:
            return answer
        else:
            if i-1 in reserve:
                answer+=1
                reserve.remove(i-1)
            elif i+1 in reserve:
                answer+=1
                reserve.remove(i+1)
    return answer

print(solution(n,lost,reserve))