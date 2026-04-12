# step2 別解およびコメント予測

そういえばpythonのライブラリにbisectがあるのを忘れていた。お手軽。
基本的なアルゴリズムはstep1で自分が書いたのと一緒に見える
ソースコード（https://github.com/python/cpython/blob/3.14/Lib/bisect.py）

```py
from bisect import bisect_left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
```

- 配列がかなり小さいなら、配列の数え上げとかmidの計算がある二分探索より、線形に探索したほうが速くないかなどと思ったり
- マジだった。だいたい20要素ぐらいまでは線形の方が速いみたい。
- (https://discord.com/channels/1084280443945353267/1192736784354918470/1199372352123850752)


- 続いて、過去のコメントを参照したり、予測したりしてみる
- 半開区間だけじゃなく閉区間でも開区間でも実装できるか 
 - ループ不変条件のバリエーション、それぞれの不変条件設定から両端点の初期化、更新式、ループ継続条件などの導出、二分探索の正当性を説明できるか
 - (https://github.com/garunitule/coding_practice/pull/41/changes#r2625314920)

あたりだろうか。実装してみる。

### 半開区間
- 不変条件「[0, left) は false、[right, n) は true、答えは常に [left, right) にある」
```py
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

### 閉区間
- 不変条件「[0, left) は false、(right, n-1] は true、未確定は [left, right]、答えは常に [left, right+1] にある」
```py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return left  # 全部Fのときはlがlen(nums)になって正しく返る
```

### 開区間
- 不変条件「ループ中、常にlは最大のfalse側、rは最小のtrue側、答えは常に (l, r) にある」
```py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
    
        while right - left > 1:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle
            else:
                right = middle
            
        return right
```
