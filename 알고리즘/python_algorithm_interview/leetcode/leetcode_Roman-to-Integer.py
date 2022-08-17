# leetcode_Roman-to-Integer 문제풀이
# 2022-08-14

class Solution:
    def romanToInt(self, s: str) -> int:
        # 변환 할 딕셔너리
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,            
        }
        
        answer = 0
        
        for i in range(len(s)-1):
            # I 다음 V나 X가 오면 빼기
            if (s[i] == 'I') and (s[i+1] == 'V' or s[i+1] == 'X'):
                answer -= roman_dict[s[i]]
                
            
            # X 다음 L나 C가 오면 빼기
            elif (s[i] == 'X') and (s[i+1] == 'L' or s[i+1] == 'C'):
                answer -= roman_dict[s[i]]
                
            # C 다음 D나 M가 오면 빼기
            elif (s[i] == 'C') and (s[i+1] == 'D' or s[i+1] == 'M'):
                answer -= roman_dict[s[i]]
                
            # 나머진 그냥 다 더하기
            else:
                answer += roman_dict[s[i]]
                
        
        answer += roman_dict[s[len(s)-1]]
        
        return answer
  