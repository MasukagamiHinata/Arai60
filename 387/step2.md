# step2
### 修正&コメント予測

### 単純な数え上げ
```py
# この解法に関してはやはり、毎回countを呼び出すのがどうか、というところあたりか
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, char in enumerate(s):
            if s.count(char) == 1:
                return i
        
        return -1
```

### defaultdict
```py
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_frequency = defaultdict(int)

        for char in s:
            char_frequency[char] += 1

        for i, char in s:
            if char_frequency[char] == 1:
                return i

        return -1 
```

### Counter
```py
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_frequency = Counter(s)
        # こちらは変数名がふさわしいかどうか。char_to_countでもいいかもしれない。

        for i, char in enumerate(s):
            if char_frequency[char] == 1:
                return i

        return -1
```
