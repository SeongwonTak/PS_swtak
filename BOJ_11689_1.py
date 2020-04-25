# https://www.acmicpc.net/problem/11689
# Euler-phi function 구현하기
def get_ans(num):
    goal = num
    i = 2
    while i*i <= num:
        if num % i == 0:
            goal = goal * (i-1) // i
            while num % i == 0:
                num = num // i
        if i == 2:
            i = i+1
        else:
            i = i+2
    if num == 1:
        print (goal)
    else:
        print (goal * (num-1) // num)

def main():
    num = int(input())
    if num == 1:
        print(1)
    else:
        get_ans(num)

if __name__ == "__main__":
    main()