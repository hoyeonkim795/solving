# linked list
class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소

class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드
        self.tail = None # 마지막 노드
        self.size = 0  # 노드의 수

    def insert_front(self, item):
        if self.is_empty():  # 첫 노드로 삽입
            self.head = self.Node(item, None)  # head가 새 노드 참조

def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return
    cur = lst.head
    while cur is not None: # while cur.next is not None: 이면 4까지 출력
        print(cur.data, end=' ')
        cur = cur.next
    print()

def insertLast(lst, new): # new : 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # else 문 뒤 코드 순서 바뀌면 안된다!!
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

def insertAt(lst, idx, new): # idx : 인덱스 값
    # 빈리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막 추가하는 경우, idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    else:
        # 중간에 추가하는 경우 (head, tail 변화 X)
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

def search(lst, target):
    cur = lst.head
    for _ in range(target):
        cur = cur.next
    return cur.data

def change(lst, idx, num):
    cur = lst.head
    for _ in range(idx):
        cur = cur.next
    cur.data = num

def deleteLast(lst):
    if lst.head is None: return
    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None: # list 한개일 경우 pre.next 에서 오류나기에 걸러주기
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
        lst.size -= 1


def deleteFirst(lst):
    if lst.head is None: return
    # 노드가 1개 일 경우 주의하기
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None

    lst.size -= 1


def deleteAt(lst, idx):
    if lst.head is None or idx == 0:
        deleteFirst(lst)
    elif idx >= lst.size:
        deleteLast(lst)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1


for tc in range(int(input())):
    N, M, L = map(int, input().split())
    lst = LinkedList()
    putlst = list(map(int, input().split()))
    for i in range(len(putlst)):
        insertLast(lst, Node(putlst[i]))
    for m in range(M):
        plus = list(map(str, input().split()))
        plus[1] = int(plus[1])
        if len(plus) == 3:
            plus[2] = int(plus[2])
            if plus[0] == 'I':
                insertAt(lst, plus[1], Node(plus[2]))
            else:
                change(lst, plus[1], plus[2])
        else:
            deleteAt(lst, plus[1])
    if lst.size <= L:
        result = -1
    else:
        result = search(lst, L)
    print('#{} {}'.format(tc + 1, result))