# 여기에 필요한 모듈을 추가합니다.
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(n):
            self.number_line = random.sample(range(1,46),6)
            self.number_lines.append(self.number_line)
            

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        
        print(f'''
==========================================
             제 {draw_number} 회 로또
==========================================
추첨일 : {self.get_draw_date(draw_number)[0]}/{self.get_draw_date(draw_number)[1]}/{self.get_draw_date(draw_number)[2]} (토)
==========================================
        ''')
        for i in range(len(self.number_lines)):
            print(f'{chr(65+i)} : {self.number_lines[i]}')

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        self.main_numbers = self.get_lotto_numbers(draw_number)[0]
        self.bonus_number = self.get_lotto_numbers(draw_number)[1]
        print(f'''
==========================================
당첨 번호 : {self.main_numbers} + {self.bonus_number}
==========================================
''')
        for i in range(len(self.number_lines)):
            self.same_main_counts = self.get_same_info(self.main_numbers, self.bonus_number, self.number_lines[i])[0]
            self.is_bonus = self.get_same_info(self.main_numbers, self.bonus_number, self.number_lines[i])[1]
            ranking = self.get_ranking(self.same_main_counts, self.is_bonus)

            if ranking == 1:
                print(f'''{chr(65+i)} : 6개 일치 (1등 당첨!)''')
            elif ranking == 2:
                print(f'''{chr(65+i)} : 5개 일치 + 보너스 번호 일치 (2등 당첨!)''')                      
            elif ranking == 3:
                print(f'''{chr(65+i)} : 5개 일치 (3등 당첨!)''')
            elif ranking == 4:
                print(f'''{chr(65+i)} : 4개 일치 (4등 당첨)''')
            elif ranking == 5:
                print(f'''{chr(65+i)} : 3개 일치 (5등 당첨)''')
            else:
                print(f'''{chr(65+i)} : {self.same_main_counts}개 일치 (낙첨)''')
    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto_info = json.load(lotto_json)
        year = lotto_info['drwNoDate'][0:4]
        month = lotto_info['drwNoDate'][5:7]
        day = lotto_info['drwNoDate'][8:10]
        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto_goal = json.load(lotto_json)
        main_numbers = []
        for i in range(6):
            main_numbers.append(lotto_goal[f'drwtNo{i+1}'])
        main_numbers = sorted(main_numbers)
        bonus_number = lotto_goal['bnusNo']
        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False
        for i in range(6):
            if line[i] in main_numbers:
                same_main_counts += 1
            if line[i] == bonus_number:
                is_bonus = True
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        if same_main_counts == 6:
            ranking = 1
        elif same_main_counts == 5:
            if is_bonus == True:
                ranking = 2
            else:
                ranking = 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5
        else:
            ranking = -1
        return ranking
