def salt(percent, mass):
    return percent / 100 * mass
# 소금, 물 총량
salt_sum = 0
mass_sum = 0
# 최대 5개 제한 만들기 위해
numbers = 1

while numbers != 6:
    user = input(f'{numbers}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
    #입력 받은 것이 Done이면 그만
    if user == 'Done':
        break
    #입력 받은 정보 중 농도와 소금물 분리
    info = user.split('% ')
    # 농도
    percent = int(info[0])
    # 소금물
    mass = int(info[1].rstrip('g'))
    
    numbers += 1
    # 소금과 소금물 총량
    salt_sum += salt(percent, mass)
    mass_sum += mass

print(f'{round(salt_sum/mass_sum*100, 2):.2f}% {round(mass_sum, 2):.2f}g')
