# 요세푸스 문제
# https://www.acmicpc.net/problem/1158
# 그저 구현하면 되는 문제로 추정
# 하지만 while로 짜니 효율이 너무 바닥.

def main():
    num, jump = map(int, input().split())
    people_num = []
    people_exit = [0] * num
    people_rid = []
    pointer = 0  # 0번부터 시작임을 잊지말자
    for i in range(0, num):
        people_num.append(i+1)

    while sum(people_exit) != num:
        check = 0
        while check < jump:
            if people_exit[pointer] == 0:
                check += 1
                pointer = (pointer + 1) % num
            else:
                pointer = (pointer + 1) % num
        if pointer == 0:
            pointer = num-1
        else:
            pointer = pointer-1
        people_exit[pointer] = 1
        people_rid.append(people_num[pointer])

    print("<", end="")
    for i in range(0, num):
        if i == (num - 1):
            print(people_rid[i], end=">")
        else:
            print(people_rid[i], end=", ")


if __name__ == "__main__":
    main()
