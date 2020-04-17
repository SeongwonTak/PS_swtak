# 2178_응용
# BOJ_7576 토마토
# 최적화를 어떻게 해야 할지 모르겠다
def solve(tomatoes, n, m):
    way_x = [-1, 1, 0, 0]  # 좌 / 우 / 상 / 하 x값 변화
    way_y = [0, 0, -1, 1]  # 좌 / 우 / 상 / 하 y값 변화
    visited = [[False] * m for _ in range(n)]
    next_block = []
    end_judge = 1
    # 첫 시작점들은 1인 좌표들에 대해서 넣어야 한다.
    for i in range(0, n):
        for j in range(0, m):
            if tomatoes[i][j] == 1:
                next_block.append([i, j])
            elif tomatoes[i][j] == 0:
                end_judge = 0

    if end_judge == 1:  # 시작하자마자 끝
        return 0

    else:  # 이제 돌아줘야 함
        day_val = 0
        while next_block:  # 더 꺼낼게 없을 때 까지
            x, y = next_block.pop(0)  # 꺼낼 거의 첫번째 위치
            if not visited[x][y]:
                visited[x][y] = True
                day_val = tomatoes[x][y]  # 지금 까지 걸린일자

                for i in range(4):
                    # 일단 4 방향중 하나를 들어가자
                    new_x = x + way_x[i]
                    new_y = y + way_y[i]
                    # 영역이 넘어갔으면 Fail
                    if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                        continue

                    if not visited[new_x][new_y]:
                        new_day_val = tomatoes[new_x][new_y]

                        if new_day_val == -1:  # 벽은 돌지 않아요
                            continue

                        elif new_day_val == 0 or day_val + 1 < new_day_val:  # 역류방지구문
                            tomatoes[new_x][new_y] = day_val + 1  # 이게 실행된다는 건, 새로운 길이다.
                            next_block.append([new_x, new_y])  # val + 1이 같거나 크다는건 이미 체크한 칸

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
            return (day_val-1)


def main():
    m, n = map(int, input().split())
    tomatoes = []
    for i in range(n):
        tomato = list(map(int, input().split()))
        tomatoes.append(tomato)

    print(solve(tomatoes, n, m))

if __name__ == "__main__":
    main()