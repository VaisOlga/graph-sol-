
import itertools

def Dijkstra(n, start, distance_matrix, cost, inf):
    used = [False] * n
    dist = [inf] * n
    dist[start] = 0
    for i in range(0, n):
        v = -1
        for j in range(0, n):
            if(not used[j] and (v == -1 or dist[j] < dist[v])):
                v = j
        used[v] = True
        for j in range(0, n):
            if(distance_matrix[v][j] != 0):
                dist[j] = min(dist[j], dist[v] + distance_matrix[v][j])
    for i in range(0, n):
        cost[start][i] = dist[i]

def func(p, cost):
    res = cost[0][p[0]] + cost[p[-1]][0]
    for i in range(1, len(p)):
        res += cost[p[i - 1]][p[i]]
    return res
        
def main():
    n = int(input())
    distance_matrix = []
    for i in range(0, n):
        distance_matrix.append([int(item) for item in input().split()])
                                 
    mmax = 0
    for i in range(0, n):
        for j in range(0, n):
            mmax = max(mmax, distance_matrix[i][j])
    inf = mmax * (2 * n + 1)              
    cost = [[inf] * n for i in range(0, n)]
    
    for i in range(0, n):
        Dijkstra(n, i, distance_matrix, cost, inf)
    
    p = list(itertools.permutations([item for item in range(1, n)]))
    
    res = inf
    for i in range(0, len(p)):
        res = min(res, func(p[i], cost))
    print(res)


if __name__ == '__main__':
	main()
