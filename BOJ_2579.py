# 계단 오르기
# DP일려나?
# https://www.acmicpc.net/problem/2579
def main():
    stairs = int(input())
    scores = []
    for i in range(0, stairs):
        scores.append(int(input()))

    answer = []
    for i in range(0, stairs):
        if i == 0:
            answer.append(scores[0])
        elif i == 1:
            answer.append(scores[0]+scores[1])
        elif i == 2:
            answer.append(max(scores[0]+scores[2],
                              scores[1]+scores[2]))
        else:
            answer.append(max(answer[i-2]+scores[i],
                              answer[i-3]+scores[i-1]+scores[i]))

    print(answer[stairs-1])
if __name__ == "__main__":
    main()