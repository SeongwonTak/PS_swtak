# 탑
# 스택으로 구현한다.
def main():
    num = int(input())  # 타워의 개수
    tower = list(map(int, input().split()))
    laser = [0] * num  # 정답열
    stack = [] # 진행열

    for i in range (0, num):
        if i == 0:
            stack.append([1, tower[i]])  # 첫번째 타워 입력
            laser[0] = 0  # 맨 왼쪽의 타워는 받을 것이 없어서.
        else:

            while len(stack) != 0:  # 길이가 0이 아닐 때만 유효
                if stack[-1][1] > tower[i]:  # 처음으로 바로옆 큰걸 받음
                    laser[i] = stack[-1][0]  # 그 건물 번호를 가져오고
                    stack.append([i + 1, tower[i]])  # 자기 자리를 넣음
                    break
                else:
                    stack.pop() # 땡이니 없애고 그 왼쪽 타워를 보자

            if len(stack) == 0:
                laser[i] = 0
                stack.append([i + 1, tower[i]])  # 실패했지만 탐색에 써야함

    for i in laser:
        print(i, end=" ")  # 공백출력

if __name__ == '__main__':
    main()