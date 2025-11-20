## step 1
# まずは総当たりを試す。
# 最初の要素index: 0は固定で、その次の要素と足し合わせて、それがtargetならそこで終わり。
# そうでないならその次の要素と足し合わせる。これを繰り返す。もしだめなら次はindex: 1を固定する。これで最後まで行く

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return None

        for x in range(n-1):
            for y in range(x+1, n):

                if nums[x] + nums[y] == target:
                    return [x, y] 

        return None 

# 空間計算量はO(1)、時間計算量はO(N^2)
# なにも見ず実装できた

# Hashによる解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return None

        seen_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_map:
                complement_index = seen_map[complement]
                return [complement_index, i]
            seen_map[num] = i
        return None

# 時間計算量はO(N)、空間計算量はO(N)
# 解答をチラ見して実装した。



## step2 他の人のを見てコード修正
# nitabongさん（https://github.com/tNita/arai60/pull/1）
# return Noneではなくraise Exceptionとするのは大変親切だと思った。

# Naoto Iwaseさん（https://github.com/docto-rin/leetcode/pull/11）
# 複数解へ対応することにも目が向いているのが参考になった。


# 総当たり
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 例外処理も一応あった方が嬉しいだろうか
        n = len(nums)
        if n < 2:
            raise Exception("The length of the list is insufficient.")

        for x in range(n-1):
            for y in range(x+1, n):
                if nums[x] + nums[y] == target:
                    return [x, y] 
        raise Exception("The answer doesn't exist.")


# Hash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            raise Exception("The length of the list is insufficient.")

        seen = {} # seenだけで伝わりそう
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                complement_index = seen[complement]
                return [complement_index, i]
            seen[num] = i
        raise Exception("The answer doesn't exist.")


# 複数解への対応（Hash）
from typing import List

class Solution:
    def twoSumAllPairs(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            raise Exception("The length of the list is insufficient.")

        seen_map = {}
        results = [] 
        for i, num in enumerate(nums):
            complement = target - num          
            if complement in seen_map:
                complement_index = seen_map[complement]
                results.append([complement_index, i])
            seen_map[num] = i
        if results is None:
            raise Exception("The answer doesn't exist.")      
        return results
            


## step 3 何度も書き直し
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                complement_index = seen[complement]
                return(complement_index, i)
            seen[num] = i

# 3回アクセプトされたので終了
