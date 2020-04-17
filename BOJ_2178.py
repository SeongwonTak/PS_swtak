# BOJ_2178 미로탐색_이해하기
# https://www.acmicpc.net/problem/2178
# https://daimhada.tistory.com/82를 보고 이해하는 과정

def solve(start, goal, mazes, n, m):
    way_x = [-1, 1, 0, 0]  # 좌 / 우 / 상 / 하 x값 변화
    way_y = [0, 0, -1, 1]  # 좌 / 우 / 상 / 하 y값 변화
    # 두 개를 같이 넣은 이유는 좌표는 방향이 4개니까 최대.
    next_block = []
    next_block.append(start)

    while next_block:  # 더 갈 칸이 있다면 더 간다
        x, y = next_block.pop(0)
        value = mazes[x][y]  # 그 칸이 지금까지 간 칸수일 거다.
        for i in range(4):
            # 일단 4 방향중 하나를 들어가자
            new_x = x + way_x[i]
            new_y = y + way_y[i]
            # 영역이 넘어갔으면 Fail
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                continue

            new_val = mazes[new_x][new_y]

            if new_val == 0:  # 벽은 돌지 않아요
                continue

            if new_val == 1 or value + 1 < new_val:  # 역류방지구문
                mazes[new_x][new_y] = value + 1  # 이게 실행된다는 건, 새로운 길이다.
                next_block.append([new_x, new_y])  # val + 1이 같거나 크다는건 이미 체크한 칸

    return mazes[goal[0]][goal[1]]


def main():
    n, m = map(int, input().split())
    mazes = []
    for i in range(n):
        maze = list(map(int, input().strip()))
        mazes.append(maze)

    start = [0, 0]
    goal = [n-1, m-1]
    print(solve(start, goal, mazes, n, m))

if __name__ == "__main__":
    main()