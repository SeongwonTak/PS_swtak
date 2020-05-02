# 사탕 배달, 추천받은 문제
# https://www.acmicpc.net/problem/17305
def solve(weight, threes, fives):
    maxi = 0
    end = min(len(fives)-1, weight // 5)  # 5의 최대개수, 5가 쓰일 횟수 중 적은거까지만
    for i in range(0, end+1):
        if (weight - 5 * i) % 3 == 0:
            if (weight - 5 * i) >= 0:
                j = (weight - 5 * i) // 3
                if j < len(threes):  # 3의 최대 개수까지만.
                    if maxi < fives[i] + threes[j]:
                        maxi = fives[i] + threes[j]
    return maxi

def main():
    candy, limit = map(int, input().split())
    threes = []
    fives = []
    for i in range(0, candy):
        weight, sweet = map(int, input().split())
        if weight == 3:
            threes.append(sweet)
        elif weight == 5:
            fives.append(sweet)

    threes = sorted(threes)
    threes.append(0)
    fives = sorted(fives)
    fives.append(0)
    threes.reverse()
    fives.reverse()

    for i in range(1, len(threes)):  # 가장 무거운거부터 쓰고 인덱스 쉽게 주려고..
        threes[i] = threes[i-1] + threes[i]
    for j in range(1, len(fives)):  # TLE 피하기 위한 누적 합
        fives[j] = fives[j-1] + fives[j]

    max_val = 0
    get = min(3*(len(threes)-1)+5*(len(fives)-1), limit) \
        # 사탕의 한계나, 가방의 한계 중 더 작은 것이 잴 무게다.
    for i in range(get, get-6, -1):  # 5g 이하로 차이나면 더 적은 사탕을 써서 노의미
        if i >= 0:
            val = solve(i, threes, fives)
            if val > max_val:
                max_val = val

    print(max_val)

if __name__ == "__main__":
    main()