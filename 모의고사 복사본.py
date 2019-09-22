def solution(answer):

    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]

    answer_list =[0, 0, 0]

    answer_list[0] = count(answer, A)
    answer_list[1] = count(answer, B)
    answer_list[2] = count(answer, C)
    print(answer_list)
    #모두 찾기
    # ans_list = np.array(answer_list)
    # a = max(answer_list)
    # ans = np.where(a == ans_list)

    m = max(answer_list)
    max_list = []
    for i in range(len(answer_list)):
        if m == answer_list[i]:
            max_list.append(i+1)
    return max_list

    ans = list(set(answer_list).intersection(max_list))
    return ans
def count(answer, supo):

    value = 0
    leng = len(answer)
    sl = len(supo)
    for i in range(leng):
        if answer[i] == supo[i%sl]:
            value += 1
    return value
ans = [1,1,1,1,1,1,1,1,1,1,1,1]
print(solution(ans))


