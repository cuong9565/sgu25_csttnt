from collections import deque
from queue import PriorityQueue
import numpy as np

lsStart = []
lsEnd = []
move = [[0,1],[0,-1],[1,0],[-1,0]]

def heuristic(a, lsEnd):
    i, cnt = 1, 0
    for i in range(3):
        for j in range(3):
            if lsEnd[i][j]==0: continue
            cnt += (a[i][j] == lsEnd[i][j])
            pass
    return 8 - cnt
class node:
    def __init__(self, a, g, x, y):
        self.a = tuple(map(tuple, a))
        self.x = x
        self.y = y
        self.g = g
        self.h = heuristic(a, lsEnd)
        self.f = g + self.h
    def __hash__(self):
        return hash((self.a))
    def __str__(self):
        return f"Bước {self.g}: g={self.g}; h={self.h}; f={self.f}\n{np.matrix(self.a)}"
    def __eq__(self, other):
        return isinstance(other, node) and self.a == other.a
    def __lt__(self, other):
        return self.f < other.f

def Taci(start, end):
    res = 0
    pq = PriorityQueue()
    pq.put(start)
    visited = set()
    visited.add(start)
    parent = {}
    parent[start] = -1
    while not pq.empty():
        u = pq.get()
        if u==end:
            end = u
            res = 1
            break
        for mv in move:
            x = mv[0] + u.x
            y = mv[1] + u.y
            if x>=0 and x<3 and y>=0 and y<3:
                v_a = list(map(list, u.a))
                v_a[x][y], v_a[u.x][u.y] = v_a[u.x][u.y], v_a[x][y]
                v = node(v_a, u.g+1, x, y)
                if v not in visited:
                    visited.add(v)
                    pq.put(v)
                    parent[v] = u
    if res == 1:
        i = end
        res = []
        while i!=-1:
            res.append(i)
            i = parent[i]
        for x in reversed(res):
            print(x)
    else: print("Không tìm thấy đường đi!!!")

lsStart = []
lsEnd = [[1,2,3],[4,5,6],[7,8,0]]
start = None
end = node(lsEnd, 0, 2, 2)

for i in range(1, 3+1):
    ls = list(map(int, input(f"Nhập các số phân biệt từ 0 -> 8. Mời nhập trạng thái dòng {i}: ").split(' ')))
    lsStart.append(ls)

for i in range(3):
    for j in range(3):
        if(lsStart[i][j]==0):
            start = node(lsStart, 0, i, j)
            break

Taci(start, end)