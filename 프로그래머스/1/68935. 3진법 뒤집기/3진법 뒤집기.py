def third(n):
    m_ans = ''
    
    while n > 0:
        n,mod = divmod(n,3)
        m_ans += str(mod)
    return m_ans

def solution(n):
    answer = 0
    t_ans = 0
    t_ans = third(n)
    answer = (int(t_ans,3))
    return answer