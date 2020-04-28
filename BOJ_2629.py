# 도전문제 : 양팔저울
def solve(gram):
    gram = sorted(gram)
    maximum = sum(gram)
    judge_list = [False for _ in range(maximum+1)] # 0번 안쓸거 씨발
    for i in range(0, len(gram)):
        temp_judge_list = [False for _ in range(maximum + 1)]
        if i != 0:
            temp_judge_list = [False for _ in range(maximum+1)]
            for j in range(1, maximum+1):
                if judge_list[j]:
                    temp_judge_list[j+gram[i]] = True
                    temp_judge_list[abs(j-gram[i])] = True
        for k in range(1, maximum+1):
            if temp_judge_list[k]:
                judge_list[k] = temp_judge_list[k]

        judge_list[gram[i]] = True

    return judge_list


def main():
    gram_num = int(input())
    gram = list(map(int, input().split()))
    ball_num = int(input())
    ball = list(map(int, input().split()))

    answer_list = solve(gram)

    for i in range(ball_num):
        if sum(gram) >= ball[i]:
            if answer_list[ball[i]]:
                print("Y")
            else:
                print("N")
        else:
            print("N")

if __name__ == "__main__":
    main()