# step1
### 一番最初に思いついた、enumerateを使って各文字のインデックスとキーを取得しcountで数え上げるやり方

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, char in enumerate(s):
            if s.count(char) == 1:
                return i
        
        return -1
# (個人的には)シンプルでわかりやすいが手間が多いと思う。１ループにつきいちいちcountを呼び出して走査するのは煩雑。

# "25日目に出勤してみて、なんも情報がなかったら「仕事にならない」と叫ぶでしょ"
# (https://discord.com/channels/1084280443945353267/1233603535862628432/1238208008182562927)

# 時間計算量O(N^2)
```

### defaultdictを使うやり方によって解決できる。
### 北野和紀さん(https://github.com/kitano-kazuki/leetcode/pull/15/)

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
# 事前に各文字の頻度を取得しておいて、後のforループで1回だけ出る文字と照合する作業だと煩雑ではない
# 時間計算量O(N+N)
```

### Counterというクラスがあったので使ってみる
### (http://docs.python.org/ja/3.13/library/collections.html#collections.Counter)

```py
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_frequency = Counter(s)

        for i, char in enumerate(s):
            if char_frequency[char] == 1:
                return i

        return -1
# defaultdictと考え方は同じ。どちらが好まれるかは正直わからない。処理が明示的なのはdefaultdictの方かな。
# 時間計算量O(N+N)
```
