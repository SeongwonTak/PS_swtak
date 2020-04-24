# https://www.acmicpc.net/problem/2502
# 또 DP...의 응용
def solve(day):  # 초항을 몰라서 ax+by에서 계수를 잡는다.
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1
    for i in range(2, day):
        x3 = x1+x2
        y3 = y1+y2
        x1 = x2
        x2 = x3
        y1 = y2
        y2 = y3
    return x3, y3

def main():
    day, cake = map(int, input().split())

    a, b = solve(day)

    day_1 = 0
    while True:
        day_1 += 1
        if (cake - a * day_1) % b == 0:
            day_2 = (cake - a * day_1) // b
            print(day_1)
            print(day_2)
            break

if __name__ == "__main__":
    main()
