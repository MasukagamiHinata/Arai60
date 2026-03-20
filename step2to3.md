短い配列にsetを1回使うやり方について
特に自分では修正箇所が思い浮かばない。変数名の変更や、配列の大きさを明示するかどうか、removeかdiscardか、ぐらい？

```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            smaller = nums2
            larger = nums1
        else:
            smaller = nums1
            larger = nums2

        intersection_result = []
        exist_in_smaller = set(smaller)

        for num in larger:
            if num in exist_in_smaller:
                intersection_result.append(num)
                exist_in_smaller.remove(num)

        return intersection_result
```

二分探索については探索と判定を切り離す書き方もできるのでは

```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = sorted(nums1)
        
        intersection_result = set()
        nums2_set = set(nums2)

        for num in nums2_set:
            left = -1
            right = len(nums1)

            while right - left > 1:
                middle = (left + right) // 2
                if nums1[middle] < num:
                    left = middle
                else:
                    right = middle

            if right < len(nums1) and nums1[right] == num:
                intersection_result.add(num)

        return list(intersection_result)
```


# 何度も書き直し
```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            smaller = nums2
            larger = nums1
        else:
            smaller = nums1
            larger = nums2
        
        exist_in_smaller = set(smaller)
        intersection_result = []

        for num in larger:
            if num in exist_in_smaller:
                intersection_result.append(num)
                exist_in_smaller.remove(num)

        return intersection_result
```

```py
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = sorted(nums1)

        intersection_result = set()
        nums2_set = set(nums2)

        for num in nums2_set:
            left = -1
            right = len(nums1)

            while right - left > 1:
                middle = (left + right) // 2
                if nums1[middle] < num:
                    left = middle
                else:
                    right = middle

            if right < len(nums1) and nums1[right] == num:
                intersection_result.add(num)

        return list(intersection_result)
```
