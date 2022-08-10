### Mine
def palindrome(sentance):
    for letter in sentance:
        if letter.isalpha():
            board.append(letter.lower())
    print(board)
    for i in range(len(board)//2):
        if board[i] != board[len(board)-i-1]:
            return False
    else:
        return True

### Solve 1
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): # .isalnum() : 영문 혹은 숫자인지 판별하는 함수
            strs.append(char.lower())
    
    # Plaindrome 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True

### Solve 2
### 10장 데크 공부 후 다시 보기

### Solve 3
def isPalindorme(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s  = re.sub('[')
