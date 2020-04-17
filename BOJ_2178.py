# BOJ_2178 미로탐색_이해하기
# https://hongku.tistory.com/276 를 보고 이해하는 과정
import sys

def solve(mazes, x, y):
    way_x = [-1, 1, 0, 0]  # 좌 / 우 / 상 / 하 x값 변화
    way_y = [0, 0, -1, 1]  # 좌 / 우 / 상 / 하 y값 변화
    visited = [[0] * y for _ in range(x)]  # 진행칸 수를 넣을 거
    next_block = []
    next_block.append((0, 0))
    visited[0][0] = 1

    while next_block:  # 더 갈 칸이 있다면 더 간다
        a, b = next_block.pop(0)
        if a == x-1 and b == y-1:
            print(visited[a][b])
            sys.exit()

        for i in range(4):
            # 일단 4 방향중 하나를 들어가자
            new_x = a + way_x[i]
            new_y = b + way_y[i]
            # 영역이 넘어갔으면 Fail
            if new_x < 0 or new_y < 0 or new_x >= x or new_y >= y:
                continue

            else:
                if visited[new_x][new_y] == 0 and mazes[new_x][new_y] == 1:
                    visited[new_x][new_y] = visited[a][b] + 1
                    next_block.append((new_x, new_y))

def main():
    x, y = map(int, input().split())
    mazes = []
    for i in range(x):
        maze = list(map(int, input().strip()))
        mazes.append(maze)

    print(solve(mazes, x, y))

if __name__ == "__main__":
    main()