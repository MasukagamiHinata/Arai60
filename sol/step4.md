# step4
### レビューを受けて修正
```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_emails = set()
        # emailsが膨大なら、ワンパス処理が有効か？

        for email in emails:
            local, domain = email.rsplit("@", 1)
            # 指摘通りrsplitを使う
            # @や""をlocal名に使えるのは知らなかった。メアドの規格RFC5322も初見だった。
            # (https://github.com/yumyum116/LeetCode_Arai60/pull/3/changes#r2869255835)

            local = local.split("+", 1)
            local = local.replace(".", "")

            normalized_emails.add(f"{local}@{domain}")
        
        return len(normalized_emails)
```

### ワンパス処理
```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_emails = set()

        for email in emails:
            local_characters = []
            i = 0
            n = len(email)

            while i < n:
                c = email[i]
                if c == "@":
                    break
                elif c == "+":
                    while i < n and email[i] != "@":
                        i += 1
                    break
                elif c != ".":
                    local_characters.append(c)

                i += 1

            domain = email[i:]

            normalized_emails.add("".join(local_characters) + domain)

        return len(normalized_emails)
```

### 正規表現で、読みやすい書き方もあった。
### pluhnさん（https://github.com/plushn/SWE-Arai60/pull/14/changes#diff-281493dffeb270a1c18ce602a08e2f236f76863b5bfccca2483f4b54e097251eR61)
```py
import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_addresses = set()
        for address in emails:
            local, domain = address.split('@', maxsplit = 1)
            local = re.sub(r'\+.*', '', local)
            local = re.sub(r'\.', '', local)
            unique_addresses.add(f"{local}@{domain}")
        return len(unique_addresses)
```
