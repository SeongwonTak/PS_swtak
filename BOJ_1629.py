# 큰 자리 수 곱셈 재도전
# 이진법을 활용하여 도전한다.
# https://www.acmicpc.net/problem/1629
# a^b mod c를 구하는 문제이다.
def main():
    a, b, c = map(int, input().split())
    pow_a = []

    mod = a % c

    while b != 0:
        if b % 2 == 1:
            pow_a.append(mod)
        mod = mod ** 2 % c
        b = b // 2

    prod = 1
    for i in range (0, len(pow_a)):
        prod = (prod * pow_a[i]) % c

    print(prod % c)


if __name__ == "__main__":
    main()