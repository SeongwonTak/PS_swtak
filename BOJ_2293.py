# https://www.acmicpc.net/problem/2293
# 그리디 문제? ㄴㄴ DP가 나을듯.
def solve(money, sum):
    checks = [[0] * (sum+1) for _ in range(0, 2)]

    fill = 0 #채워야 하는 횟수를 의미. 동전 개수만큼 반복하려고
    while fill != len(money):
        total = 0
        # 첫 줄은 배수로 채우자.
        if fill == 0: #첫 동전 라인은 그냥.
            while total <= sum:
                checks[0][total] = 1
                total += money[0]
        else:
            while total <= sum:
                if total == 0:
                    checks[1][total] = 1
                elif total < money[fill]:
                    checks[1][total] = checks[0][total]
                else:
                    checks[1][total] = checks[0][total]+checks[1][total-money[fill]]
                total += 1

            for i in range(0, sum+1):
                checks[0][i] = checks[1][i]
        fill += 1

    print(checks[0][sum])

def main():
    coin, sum = map(int, input().split())
    money = []
    for i in range(0, coin):
        money.append(int(input()))
    money = sorted(money)  #일단 정렬하자.
    solve(money, sum)

if __name__ == "__main__":
    main()