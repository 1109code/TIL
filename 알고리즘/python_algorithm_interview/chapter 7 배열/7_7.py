# 두수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스 리턴
numbs = [2, 7, 11, 15]
target = [9]

# my_sol
for i in range(len(numbs)):
    for j in range(i+1, len(numbs)):
        if i == j:
            pass
        elif numbs[i] + numbs[j] == target[0]:
            result = [i, j]
            print(result)

# sol1 무차별 대입 방식인 브루트 포스, 단골 비효율 풀이
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# sol2 in을 이용한 탐색
# target - n 이 존재하는지 탐색
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

# sol3 첫 번째 수를 뺀 결과 키 조회
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target -num]:
            return [i, nums_map[target-num]]

# sol4 조회 구조 개선
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# sol5 투 포인터 이용
# 인덱스가 정렬이 안되어 있기 때문에 원래 사용 불가
# sort 해도 인덱스를 출력해야 하기 때문에 문제에 맞지 않는 풀이
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) -1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        
        else:
            return [left, right]

# sol6 Go 구현
# 시간제한에서 python으로는 안되고 다른 언어로는 될 때가 있음