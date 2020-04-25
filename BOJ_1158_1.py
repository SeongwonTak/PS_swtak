#요세푸스 문제 큐로 짜기

import queue
def main():
    num, jump = map(int, input().split())
    people_num = queue.Queue()
    answer = []

    for i in range(1, num+1):
        people_num.put_nowait(i)

    for i in range(0, num):
        for j in range(0, jump-1):
            cnt = people_num.get_nowait()
            people_num.put_nowait(cnt)
        answer.append(people_num.get_nowait())

    print("<", end="")
    for i in range(0, num):
        if i == (len(answer)-1):
            print(answer[i], end=">")
        else:
            print(answer[i], end=", ")

if __name__ == "__main__":
    main()