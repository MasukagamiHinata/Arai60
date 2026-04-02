# step2 別解探索など
- defaultdictをつかうやり方 by Claude
- エレガントだがあまりスムーズに考え方が理解できない。読み手に負荷がかかりそうではある

```py
from collection import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - k]
            freq[prefix_sum] += 1

        return count
```

### 他の人のコードも見てみる

- Kazuさん https://github.com/Kazuuuuuuu-u/arai60/pull/19/
- 考え方としてはだいたい一緒。変数名が明示的であるかどうか、ぐらいか
- if文をなくしても動きそうだが

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        sum_to_count = defaultdict(int)
        sum_seqeunce_elements = 0

        sum_to_count[0] = 1

        for num in nums:
            sum_seqeunce_elements += num
            if sum_seqeunce_elements - k in sum_to_count:
                count += sum_to_count[sum_seqeunce_elements - k]
            sum_to_count[sum_seqeunce_elements] += 1

        return count
```

- nitabongさん https://github.com/tNita/arai60/pull/16/changes
- 前日までの、すべての部分配列の和を引き継ぐ、という感じ。面白い
```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sums = defaultdict(int)
        ans = 0
        for num in nums:
            current_sums = defaultdict(int)

            for total in prev_sums:
                current_sums[total + num] += prev_sums[total]
            
            current_sums[num] += 1
            ans += current_sums[k]
            prev_sums = current_sums
        return ans
```

- かなり理解するのに時間がかかった&疲れたのでいったんここまで。要復習
