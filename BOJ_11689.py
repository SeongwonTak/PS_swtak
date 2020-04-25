# https://www.acmicpc.net/problem/11689
# Euler-phi function 구현하기
def prime_judge(num):
    judge = True
    for i in range(2, int(num ** (0.5))+1):
        if num % i == 0:
            judge = False
            break
    return judge

def get_ans(num):
    i = 2
    while i <= num:
        if prime_judge(i) and num % i == 0:
            num = num * (i-1) // i
        i = i+1
    print(num)

def main():
    num = int(input())
    if num == 1:
        print(1)
    else:
        get_ans(num)

if __name__ == "__main__":
    main()