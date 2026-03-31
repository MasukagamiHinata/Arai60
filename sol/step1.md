### step1
- Counterを使って頻度を集計したのち、frozensetで順序を無視しつつハッシュ可能にしてdictに追加していく
 - いろいろ調べて行きついた。マイナーかも。

```py
from typing import List
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = frozenset(Counter(word).items())
            groups[key].append(word)

        return list(groups.values())
```
