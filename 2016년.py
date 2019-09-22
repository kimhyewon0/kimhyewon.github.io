import datetime

def solution(a, b):
    week =["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    answer = week[(datetime.datetime(2016, a, b).weekday() +1) %7]

    return answer

a = 1
b = 3

print(solution(a,b))
#print((datetime.datetime(2016, 1, 3).weekday()+1)%7)