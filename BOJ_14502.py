# 연구소
# 취약 유형에 재도전. https://www.acmicpc.net/problem/14502
from _collections import deque

def virus(lab, row, col):
    safe_num = 0
    twos = deque()
    for i in range(0, row):
        for j in range(0, col):
            if lab[i][j] == 2:
                twos.append([i, j])

    way_x = [1, 0, -1, 0]
    way_y = [0, 1, 0, -1]

    while twos: # 더 없을 때까지
        x, y = twos.popleft()

        for i in range(0, 4):  # 4방향을 들어간다.
            new_x = x+way_x[i]
            new_y = y+way_y[i]

            if new_x<0 or new_x>=row or new_y<0 or new_y>=col:  # 범위 초과
                continue
            else:
                if lab[new_x][new_y] == 0:  # 바이러스 옆의 전염 안된 칸은
                    lab[new_x][new_y] = 3  # 전 염 피 망
                    twos.append([new_x, new_y])

    for i in range(0, row):
        for j in range(0, col):
            if lab[i][j] == 0:
                safe_num += 1
            elif lab[i][j] == 3:
                lab[i][j] = 0

    return safe_num

def main():
    row, col = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(row)]
    zeros = [(i, j) for i in range (row) for j in range (col) if lab[i][j] == 0]  \
        # 0 위치마다 벽 세울거 일단.
    max_safe = 0

    for i in range(0, len(zeros)-2):
        for j in range(i+1, len(zeros)-1):
            for k in range(j+1, len(zeros)):  # 3개의 벽을 지정한다.

                lab[zeros[i][0]][zeros[i][1]] = 1
                lab[zeros[j][0]][zeros[j][1]] = 1
                lab[zeros[k][0]][zeros[k][1]] = 1

                safe_num = virus(lab, row, col)  # 전염

                if safe_num > max_safe:  # 생존칸 값 최대니?
                    max_safe = safe_num

                lab[zeros[i][0]][zeros[i][1]] = 0  # 복구
                lab[zeros[j][0]][zeros[j][1]] = 0
                lab[zeros[k][0]][zeros[k][1]] = 0

    print(max_safe)
if __name__ == "__main__":
    main()
