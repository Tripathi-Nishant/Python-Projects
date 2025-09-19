import math

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def lower_chain(points):
    pts = sorted(points)
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    return lower 

def perimeter_lower_chain(chain):
    return sum(math.hypot(chain[i+1][0]-chain[i][0], chain[i+1][1]-chain[i][1])
               for i in range(len(chain)-1))

n = int(input().strip())
pts = [tuple(map(int, input().split())) for _ in range(n)]
chain = lower_chain(pts)
perim = perimeter_lower_chain(chain)
print(int(math.floor(perim + 0.5)))  
