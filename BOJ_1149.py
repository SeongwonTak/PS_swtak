# RGB 거리
# DP문제!!
def main():
    home = int(input())
    red = [0] * home
    green = [0] * home
    blue = [0] * home

    answer = [0, 0, 0]
    for i in range(0, home):
        red[i], green[i], blue[i] = map(int, input().split())

    for j in range(0, home):
        old_answer = [0, 0, 0]
        for k in range(0, 3):
            old_answer[k] = answer[k]

        if j == 0:
            answer[0] = red[0]
            answer[1] = green[0]
            answer[2] = blue[0]
        else:
            answer[0] = min(red[j]+old_answer[1], red[j]+old_answer[2])
            answer[1] = min(green[j]+old_answer[0], green[j]+old_answer[2])
            answer[2] = min(blue[j]+old_answer[0], blue[j]+old_answer[1])

    print(min(answer[0], answer[1], answer[2]))

if __name__ == "__main__":
    main()