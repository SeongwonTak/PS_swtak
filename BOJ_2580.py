# 드디어 스도쿠 문제에 도전한다.
# https://www.acmicpc.net/problem/2580
# 똑같이 백트래킹으로 답을 출력한다.
# 다 세면 너무 돌아간다. 거꾸로 넣으려는 수가 있나 보자.
import sys
def rowcol(i, j, val):
    for k in range(9):
        if val == sudoku[i][k] or val == sudoku[k][j]:
            return False
    return True

def box(i, j, val):
    #먼저 어느 박스인지 좌표 계산
    box_x = i // 3 * 3
    box_y = j // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[box_x+i][box_y+j]:  # 넣을려는 값이 있어?
                return False
    return True

def solve(solved_zero):
    if solved_zero == len(zeros):
        for i in range(0, 9):
            for j in range(0, 9):
                print(sudoku[i][j], end=" ")
            print()
        sys.exit() # 하나만 풀면 종료
    else:
        for trying in range(1, 10):  # 값을 시도한다 1~9로
            sol_x = zeros[solved_zero][0]  # 풀어야할 x 위치
            sol_y = zeros[solved_zero][1]  # 풀어야할 y 위치

            if rowcol(sol_x, sol_y, trying) and box(sol_x, sol_y, trying):
                sudoku[sol_x][sol_y] = trying  # 이거라고 가정하고
                solve(solved_zero+1) # 다음 0 칸으로 들아간다.
                sudoku[sol_x][sol_y] = 0  # 풀지 못하면 다시 빈칸\
                # 이 때 제로 리스트는 다시 원상복구된다.

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(0, 9):
    for j in range(0, 9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))
solve(0)

