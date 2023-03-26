import collections


class LinkNode:  # 定义链表结点类
    def __init__(self, val, next_=None):
        self.val = val  # 该结点的值
        self.next = next_  # 该结点指向下一个结点的指针


def list2link(alist: list) -> LinkNode:  # 列表转链表
    head = LinkNode(alist[0])  # 把列表第一个元素的值存到链表中，此时第一个结点的next为None
    p = head  # 拿到head结点
    for i in range(1, len(alist)):
        p.next = LinkNode(alist[i])  # 把当前结点的指针指向下一个结点
        p = p.next  # 拿到下一个结点
    return head  # 返回首结点


