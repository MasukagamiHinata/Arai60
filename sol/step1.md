# step1

素直に二分探索を書く。
気を付けたことは次の通り

>1. 二分探索を、 [false, false, false, ..., false, true, true, true, ..., true] と並んだ配列があったとき、 false と true の境界の位置を求める問題、または一番左の true の位置を求める問題と捉えているか？
>2. 位置を求めるにあたり、答えが含まれる範囲を狭めていく問題と捉えているか？
>3. 範囲を考えるにあたり、閉区間・開区間・半開区間の違いを理解できているか？
>4. 用いた区間の種類に対し、適切な初期値を、理由を理解したうえで、設定できるか？
>5. 用いた区間の種類に対し、適切なループの条件式を、理由を理解したうえで、設定できるか？
>6. 用いた区間の種類に対し、範囲を狭めるためのロジックを、理由を理解したうえで、適切に記述できるか？
https://discord.com/channels/1084280443945353267/1196498607977799853/1269532028819476562

また、解く前に二分探索についてClaudeと一緒におさらいしたので、すんなり解くことができた。

```py
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (right + left) // 2

            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        return left
```
