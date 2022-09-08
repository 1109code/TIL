import math

# 두 점 사이의 거리
# 리스트
def distance(target1, target2):
    dist = math.sqrt((target1[0] - target2[0])**2 + (target1[1] - target2[1])**2)
    return dist

# 예, 둔각 각도 계산
def tri_angle(a, b, c):
    ang = math.acos((a**2 + b**2 - c**2)/(2*a*b))
    return ang*180/math.pi

# 분신술
def shadow(hole, target):
    global d
    # 1사분
    # 빗면 c
    c = distance(hole, target)
    # 가로 a (x길이)
    a = abs(target[0]-hole[0])
    # 세로 b (y길이)
    b = abs(target[1]-hole[1])

    if hole[0] > target[0] and hole[1] > target[1]:
        shadow_pos = [target[0]-d * a/c, target[1]-d * b/c]
        return shadow_pos
    # 2사분
    elif hole[0] < target[0] and hole[1] > target[1]:
        shadow_pos = [target[0]+d * a/c, target[1]-d * b/c]
        return shadow_pos
    
    # # 3사분
    elif hole[0] < target[0] and hole[1] < target[1]:
        shadow_pos = [target[0]+d * a/c, target[1]+d * b/c]
        return shadow_pos
    
    # # 4사분
    elif hole[0] > target[0] and hole[1] < target[1]:
        shadow_pos = [target[0]-d * a/c, target[1]+d * b/c]
        return shadow_pos
        
d = 5.73
hole = [28, 30]
target = [17, 5]
white = [2, 2]
shadow_ball = shadow(hole, target)
print(shadow_ball)
a = distance(hole, target)
b = distance(target, white)
c = distance(hole, white)
print(tri_angle(a, b, c))
