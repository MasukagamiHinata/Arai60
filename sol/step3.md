# step3 他人のコードを読む
- Manatoさん https://github.com/Manato110/LeetCode-arai60/pull/12/changes
 - joinとsortと使う。keyが文字列であり、直観的に読みやすいと感じた。
 - 処理もわかりやすい。

```py
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for string in strs:
            anagram_key = "".join(sorted(string))        
            anagram_group[anagram_key].append(string)
        
        return list(anagram_group.values())
```

- 
