#### 問題：82. Remove Duplicates from Sorted List II（https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/）

# step1：なにも見ないで書く

# 基本形はIと一緒でよい。単独のポインターでは重複を飛ばして繋ぎ変えるところまでできないので、もう一つ、遅れて動く役が必要。
# 1, 1, 1, 2, 3といった先頭から重複が続くリストに対応するためにも、仮の先頭を用意する必要がある。
# ただ実装をどうしたらいいかわからないので、やむなく他の人のコードを読むことにした

# 参考にしたソースコード
# yterashimaさん(https://github.com/TrsmYsk/leetcode/pull/4/commits)
# シンプルな解法だと思うので、基本形を参考にさせてもらった。条件分岐の書き方など。

# Naoto Iwaseさん(https://github.com/docto-rin/leetcode/pull/4/commits)
# ネストされた関数を使っているけど、個人的に若干読みにくいと感じるので、今回は用いない。
# stackを用いた解法および書き方のバリエーションについて勉強になった。別解として参考にした。

# Nanaeさん(https://github.com/nanae772/leetcode-arai60/pull/5/commits)
# ロジックの流れがわかりやすく読みやすかったので、これも実装に際して参考にした。


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = head 
        pred = dummy
        while node is not None:
            if node.next is not None and node.val == node.next.val:
                while node.next is not None and node.val == node.next.val:
                    node = node.next
                pred.next = node.next
            else:
                pred = node
            node = node.next
        return dummy.next


# step2: 他の人のコードを読んで別解探索と修正
# yterashimaさん(https://github.com/TrsmYsk/leetcode/pull/4/commits)
# Naoto Iwaseさん(https://github.com/docto-rin/leetcode/pull/4/commits)
# Nanaeさん(https://github.com/nanae772/leetcode-arai60/pull/5/commits)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        IMPOSSIBLE_VAL = -100
        dummy = ListNode(IMPOSSIBLE_VAL, head) #nanaeさんの解答を参考に、確実の取り得ない値にした
        curr = head # predとの対比でcurrに。
        pred = dummy
        while curr is not None:
            if ( 
                curr.next is not None 
                and curr.val == curr.next.val
            ):
                while (
                    curr.next is not None 
                    and curr.val == curr.next.val
                ):
                    curr = curr.next
                pred.next = curr.next # 重複をまとめてスキップ  
            else:
                pred = curr
            curr = curr.next
        return dummy.next

# 再帰を用いた解法(Geminiに相談しながら解いた)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse_and_delete(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None or node.next is None:
                return node

            if node.val == node.next.val:  
                while (
                    node.next is not None 
                    and node.val == node.next.val
                ):
                    node = node.next
                return recurse_and_delete(node.next)
            
            else:
                node.next = recurse_and_delete(node.next)
                return node
        
        return recurse_and_delete(head)

# step3: 再び何も見ないで書く。アクセプトされてもとりあえず3回は書き直す
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        IMPOSSIBLE_VAL = -100
        dummy = ListNode(IMPOSSIBLE_VAL, head)
        curr = head
        pred = dummy
        while curr is not None:
            if (
                curr.next is not None
                and curr.val == curr.next.val
            ):
                while (
                    curr.next is not None
                    and curr.val == curr.next.val
                ):
                    curr = curr.next
                pred.next = curr.next
            else:
                pred = curr
            curr = curr.next
        return dummy.next
