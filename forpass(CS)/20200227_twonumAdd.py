# encoding :utf-8
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

【思路】：1.先根据链表逆序获取得到数值num1、num2，
        2.将两个数求和得到twosum
        3.将数值的位数作为链表的个数，排除首位为零的情况
        4.关键在于如何处理链表的位数
           可以在读取一个链表的过程中记录位数，并把数赋给num1
           可以直接对链表直接进行加减 有10往下一位加一
【问题】：其中遇到两个问题
      1.如何对单链表的操作 l1.next指向下一个就没办法完成前面指向的计算
      2.如何在特殊情况 例如进位中加到1
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 1.不是最后一个结点 大于9 向后一位进1 保留当前值减去10以后的个位数 指向链表L的指针p->next所指向的值进一（+1）；小于九正常走
        # 2.是最后一个结点   大于9 同上处理，但对最后一个结点的处理为，新增一个结点为1的值（ListNode）
        # 3.有两种计算的特殊问题 含零问题：L1链表中含有0 L2链表中含有0 两个链表中都含有0
        #                     两个链表长度不同：优先长的 不足以零补齐 结束条件要再判断一下只有当两个链表都没有下个结点时候才结束 还有那就继续计算 没有值的作零处理 缺位补零思想
        #  默认处理 将l3设为两个单链表中较短的 l5为长 长度以l5为准
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            p5, p3 = l1, l2
            count, count1 = 1

            # flag = p3.val + p5.val
            # if flag != 0:
            #     while p3.next != None:
            #         count += 1
            #     while p5.next != None:
            #         count1 += 1
            #     # 以p5的长度为标准
            #     if count < count1:
            #         p3 = l1
            #         p5 = l2
            #     while p5.next != None:
            #         p5.val += p3.val
            #         if p5.val > 9:
            #             p5.val -= 10
            #             p5.next.val += 1
            #         if p3.next == None:
            #             p3.next = ListNode(0)
            #         p3 = p3.next
            #         p5 = p5.next
            #     p5.val += p3.val
            #     if p5.val > 9:
            #         p5.val -= 10
            #         p5.next = ListNode(1)
            #     return l1
            # else:
            #     return l1


#         if ( l3.val != 0 )|(l4.val != 0 ):
#             while l3.next != None:
#                 l3.val += l5.val
#                 if l3.val > 9:
#                     l3.val -= 10
#                     l3.next.val += 1
#                 if l5.next != None:
#                     l3 = l3.next
#                     l5 = l5.next
#             l3.val += l5.val
#             if l3.val > 9:
#                 l3.val -= 10
#                 l3.next= ListNode(1)
#                 return l1
#             return l1
#             # 同时等于零 相加就完了
#         elif l3.val == 0 or l5.val == 0:
#             l3.val += l5.val
#             return l1
#         else:
#             # 有一个等于零的情况
#             while l3.next != None:
#                 l3.val += l5.val
#                 if l3.val > 9:
#                     l3.val -= 10
#                     l3.next.val += 1
#                 if l5.next != None:
#                     l3 = l3.next
#                     l5 = l5.next
#             l3.val += l5.val
#             if l3.val > 9:
#                 l3.val -= 10
#                 l3.next= ListNode(1)
#                 return l1
#             return l1
num2 = Solution()
L1 = ListNode()
L2 = ListNode()
num2.addTwoNumbers(L1,L2)
