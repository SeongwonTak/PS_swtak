# 다각형의 면적
# 적분을 유사하게 적용하자.
# 사실 외적으로도 풀리지만, 오목다각형일때 곤란한걸, 그냥 쉽게 해결하자.
# 사실은 행렬식의 값이기도 하다. 단, 평행사변형 형태로.
# https://www.acmicpc.net/problem/2166


def main():
    vrtx = int(input())
    points = []
    for i in range(0, vrtx):
        points.append(list(map(int, input().split())))


    #y좌표 옮기기
    min_y = points[0][1]
    for i in range(0, vrtx):
        if points[i][1] < min_y:
            min_y = points[i][1]
    for i in range(0, vrtx):
        points[i][1] = points[i][1] - min_y
    area = 0

    for i in range(1, vrtx):
            area += (points[i][0]-points[i-1][0]) *\
                (abs(points[i][1])+abs(points[i-1][1])) * 1/2
    area += (points[0][0]-points[vrtx-1][0]) *\
                (abs(points[0][1])+abs(points[vrtx-1][1])) * 1/2

    print(abs(area))

if __name__ == "__main__":
    main()