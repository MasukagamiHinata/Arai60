## step 1 

# ダミーとwhileを用いる解法(LinkedList系でこれまでやってきたこと)しか思いつかなかった。
# ひとつひとつノードを処理する。繰り上がりには新しい変数を用意するといい。
# 参考にした人
# Naoto Iwaseさん(https://github.com/docto-rin/leetcode/pull/5)
# nanaeさん(https://github.com/nanae772/leetcode-arai60/pull/6)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val_l1 = l1.val if l1 is not None else 0 # ノードが存在しなければ０を割り当てる
            val_l2 = l2.val if l2 is not None else 0

            SUM_val = val_l1 + val_l2 + carry
            carry = SUM_val // 10 # carryを更新
            new_node_val = SUM_val % 10

            current.next = ListNode(new_node_val)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next

#空間計算量はO(1)、時間計算量はO(N)


## step 2
# コードの修正および別解探索

# 参考にした人
# Naoto Iwaseさん(https://github.com/docto-rin/leetcode/pull/5)
# nanaeさん(https://github.com/nanae772/leetcode-arai60/pull/6)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None) # 0よりも、無効な-1の方がダミーとしてはいい。nextがNoneを指していることも明示する。
        node = dummy # previousとの対比でもないので、nodeという命名でよい
        carry = 0 

        while l1 is not None or l2 is not None or carry != 0:
            val_l1 = l1.val if l1 is not None else 0 # digitという命名もされていたが、valでも大きな問題はない気がする
            val_l2 = l2.val if l2 is not None else 0

            sum_val = val_l1 + val_l2 + carry
            carry = sum_val // 10
            new_node_val = sum_val % 10

            node.next = ListNode(new_node_val)
            node = node.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next

# 再帰的な書き方もあるだろう。
# 参考にした人
# やすさん(https://github.com/yas-2023/leetcode_arai60/blob/9f65a84c5bb33f6735eb4fe6844b015533316dc0/2/step2_1_recursion.py)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_digit_recursive(l1, l2, carry):
            if l1 is None and l2 is None and carry = 0:
                return None

            val_l1 = l1.val if l1 is not None else 0 
            val_l2 = l2.val if l2 is not None else 0

            sum_val = val_l1 + val_l2 + carry
            new_carry = sum_val // 10
            new_val = sum_val % 10

            node = ListNode(new_val)
            
            next_l1 = l1.next if l1 is not None else None
            next_l2 = l2.next if l2 is not None else None

            node.next = add_digit_recursive(next_l1, next_l2, new_carry)

            return node

        return add_digit_recursive(l1, l2, 0) 
