# 연습문제2_itoa_문제풀이
# 2022-08-12

def itoa(i):
    if i == 0:
            return '0' 
        
    if i < 0:
        flag = False
        i = -(i)
    else:
        flag = True
    
    result = ''

    while i:
        i, remainder = i//10, i % 10
        result = chr(ord('0') + remainder) + result
    
    if flag:
        return result
    else:
        return '-'+result