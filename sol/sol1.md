# step1
# 普通に、組み込み関数のsplitとreplaceを使って解く
```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_emails = set()

        for email in emails:
            # if email.count("@") != 1: 
                # raise ValueError(f"Invalid email: {email}")
            
            local, domain = email.split("@")

            local = local.split("+", 1)[0]
            local = local.replace(".", "")

            normalized_emails.add(local + "@" + domain)

        return len(normalized_emails)
```

# 正規表現を使うやり方もあるらしい
# 読みにくい…練習にはいいが…
```py
import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def canonicalize(email):
            match = re.match(r"^([^+@]+)(?:\+[^@]*)?@(.+)$", email)
            if not match:
                raise ValueError("invalid input")
    
            local = match.group(1).replace(".", "")
            domain = match.group(2)
            return f"{local}@{domain}"

        unique_emails = set()
        for email in emails:
            unique_emails.add(canonicalize(email))
        return len(unique_emails)
```
