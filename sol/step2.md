### step2 コード修正および別案
- frozensetを使わずsortするやり方がある。Naoto Iwaseさん（https://github.com/naoto-iwase/leetcode/pull/12/changes#diff-fe2d4c2dc887ab0e20b792b5554f8825a47ae7cb967d7cce8e23a4ea022e660fR82）
 - frozensetってそこまで知名度なさそうだし、意図がわかりにくい気がする
 - 構成や変数名にも少し違和感(keyとか)があるので変更

```py
from typing import List
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counter = Counter(word)
            anagram_key = tuple(sorted(counter.items())) # keyのみだと、ここで行われてる処理を表現しきれない気がした。
            groups[anagram_key].append(word)

        return list(groups.values())
```


- 固定長
 - 問題を解くことに最適化されすぎな解法だと思う（https://github.com/Fuminiton/LeetCode/pull/12#discussion_r1971612972）。
 - 大文字とか記号が来た場合は別の解があるだろう

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord("a")] += 1
            
            anagram_key = tuple(counts)
            groups[anagram_key].append(word)

        return list(groups.values())
```
