from collections import deque
from queue import PriorityQueue

n = int(input("Mời bạn nhập số đĩa: "))

def heuristic(c):
    t, f, i = 0, 0, n
    for x in reversed(c[2]):
        if x==i: t+=1
        else: f+=1
        i-=1
    return f + (n-t)

class node:
    def __init__(self, c, g):
        self.c = c
        self.g = g
        self.h = heuristic(c)
        self.f = g + self.h
    def __str__(self):
        return f"Bước {self.g}: {list(map(list,self.c))}"
    def __hash__(self):
        return hash(tuple(map(tuple,self.c)))
    def __eq__(self, other):
        return isinstance(other, node) and self.c == other.c
    def __lt__(self, other):
        return self.f < other.f


def HaNoiTowel(u, end):
    pq = PriorityQueue()
    pq.put(u)
    visited = set()
    visited.add(u)
    parent = {}
    parent[u] = -1
    while(not pq.empty()):
        u = pq.get()
        if u.c == end.c:
            end = u
            break
        for i in range(3):
            for j in range(3): 
                if i!=j:
                    v_c = [deque(x) for x in u.c]
                    v_g = u.g + 1
                    if v_c[i] and ((not v_c[j]) or (v_c[i][0] < v_c[j][0])):
                        v_c[j].appendleft(v_c[i].popleft())
                        v = node(v_c, v_g)
                        if v not in visited:
                            visited.add(v)
                            pq.put(v)
                            parent[v] = u
    res = []
    x = end
    while(x!=-1):
        res.append(x)
        x = parent[x]
    for i in reversed(res):
        print(i)

start = node([deque(range(1, n+1)), deque(), deque()], 0)
end = node([deque(), deque(), deque(range(1, n+1))], 0)

HaNoiTowel(start, end)