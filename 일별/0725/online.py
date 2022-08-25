def leap_year(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return f'{n}년은 윤년입니다.'
    else:
        return f'{n}년은 윤년이 아닙니다.'