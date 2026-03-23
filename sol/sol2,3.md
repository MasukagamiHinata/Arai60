# step2
### 修正＆コメント予測

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_emails = set()
        # emailsが膨大だとsetを使うべきじゃないかもしれない

        for email in emails:
            if email.count("@") != 1: 
                raise ValueError(f"Invalid email: {email}")
            # 不正な入力への対処は気にするところかもしれない。

            local, domain = email.split("@", 1)
            # maxsplit=1のほうが意図が伝わりやすい？(＠の前後をlocalとdomainに分配)

            local = local.split("+", 1)[0]
            local = local.replace(".", "")

            normalized_emails.add(f"{local}@{domain}")
            # f-stringの方が読みやすい気がする

        return len(normalized_emails)
```

# step3
### 何度も書き直し
```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_emails = set()

        for email in emails:
            if email.count("@") != 1:
                raise ValueError(f"Invalid email: {email}")

            local, domain = email.split("@", 1)

            local = local.split("+", 1)[0]
            local = local.replace(".", "")

            normalized_emails.add(f"{local}@{domain}")

        return len(normalized_emails)
```
