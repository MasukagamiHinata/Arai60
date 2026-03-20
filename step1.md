要素の重複が無く、順序もないので、両配列をsetにし共通部分を&で得ることで簡単に解くことができる

```py
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# sol = Solution()
# result = sol.intersection([1,2,2,1], [2,2])
# print(result)
# 出力は[2]
```
あまりにも単純すぎるような気がするが
katatakuさん(https://github.com/katataku/leetcode/pull/12#discussion_r1894613102)のPRでも議論されていた↓
"片方がとても大きくて、片方がとても小さいときには、大きい方を set にするのは大変じゃないでしょうか特に大きいほうが sort 済みのときにはどうしますか。"


それを踏まえて、新しい解法(setを1回だけ、短いほうの配列に使うやり方)
setを1回だけ、短いほうの配列に使うやり方
北野和紀さん(https://github.com/kitano-kazuki/leetcode/pull/13)
ksaitoさん(https://github.com/ksaito0629/leetcode_arai60/pull/12)

```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            smaller_nums = nums2
            larger_nums = nums1
        else:
            smaller_nums = nums1
            larger_nums = nums2
        # if...以下でnums1, nums2 = nums2, nums1にすることも考えた
        # 後に続くコードでnums1,2の区別がわからなくなりそうなので配列の大きさを明示した

        exist_in_smaller = set(smaller_nums)
        intersection_result = []

        for num in larger_nums:
            if num in exist_in_smaller:
                intersection_result.append(num)
                exist_in_smaller.remove(num) 
                # discardでもいい

        return intersection_result
```


片方がsort済みなら二分探索も使える
katatakuさん(https://github.com/katataku/leetcode/pull/12)

```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection_result = set()

        for num in nums2:
            if num in intersection_result:
                continue

            left = -1
            right = len(nums1)

            while right - left > 1:
                middle = (left + right) // 2

                if nums1[middle] == num:
                    intersection_result.add(num)
                    break

                if nums1[middle] < num:
                    left = middle
                else:
                    right = middle

        return intersection_result
```
