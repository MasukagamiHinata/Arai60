# step1
- そもそも問題の意味があまり理解できずAIに聞いてしまった。そこから取り組み開始
- 愚直にブルートフォースして全部走査する以外思いつかなかった
- 時間超過でACされないので時間計算量の効率化を考える

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for l in range(n):
            summation = 0
            for r in range(l, n):
                summation += nums[r]
                if summation == k:
                    count += 1

        return count
```
- 時間計算量 O(n^2), 空間計算量O(1)
