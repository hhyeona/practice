def solution(nums):
    answer = 0
    num = len(nums)//2
    sett = set(nums)
    
    if len(sett) < num:
        answer = len(sett)
    else:
        answer = num
    return answer