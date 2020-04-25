# 2178_응용
# BOJ_7576 토마토
# 최적화를 어떻게 해야 할지 모르겠다
import queue

def solve(tomatoes, n, m):
    way_x = [-1, 1, 0, 0]  # 좌 / 우 / 상 / 하 x값 변화
    way_y = [0, 0, -1, 1]  # 좌 / 우 / 상 / 하 y값 변화
    visited = [[0] * m for _ in range(n)]
    next_block = queue.Queue()
    end_judge = 1
    # 첫 시작점들은 1인 좌표들에 대해서 넣어야 한다.
    for i in range(0, n):
        for j in range(0, m):
            if tomatoes[i][j] == 1:
                next_block.put((i, j))
            elif tomatoes[i][j] == 0:
                end_judge = 0

    if end_judge == 1:  # 시작하자마자 끝
        return 0

    else:  # 이제 돌아줘야 함
        day_val = 0
        visited[0][0] = 0
        while next_block:  # 더 꺼낼게 없을 때 까지
            (x, y) = next_block.get()  # 꺼낼 거의 첫번째 위치

            for i in range(4):
                # 일단 4 방향중 하나를 들어가자
                new_x = x + way_x[i]
                new_y = y + way_y[i]
                # 영역이 넘어갔으면 Fail
                if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                    continue

                else:
                    if visited[new_x][new_y] == 0 and tomatoes[new_x][new_y] == 0:
                        tomatoes[new_x][new_y] = 1
                        visited[new_x][new_y] = visited[x][y] + 1
                        day_val = visited[new_x][new_y]
                        next_block.put((new_x, new_y))

        # 안 된 칸이 있나 체크
        end_judge_t = 1
        for i in range(n):
            for j in range(m):
                if tomatoes[i][j] == 0:
                    end_judge_t = 0
                    break

        if end_judge_t == 0:
            return -1

        else:
            return (day_val)


def main():
    m, n = map(int, input().split())
    tomatoes = []
    for i in range(n):
        tomato = list(map(int, input().split()))
        tomatoes.append(tomato)

    print(solve(tomatoes, n, m))

if __name__ == "__main__":
    main()