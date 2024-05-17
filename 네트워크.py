from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            answer += 1
            visited[i] = True
            queue = deque([i])
            while queue:
                vx = queue.popleft()
                for nx in range(n):
                    if computers[vx][nx] == 1 and visited[nx] == False:
                        visited[nx] = True
                        queue.append(nx)
    return answer
