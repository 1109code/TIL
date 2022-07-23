def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    check_list = [0 for i in range(10)]
    for i in range(10):
        check_list[i] = f'{i}'
    
    # 

    if user_data['id'][-1] not in check_list:
        return False
    else:
        return True

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False