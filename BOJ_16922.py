# 브루트포스 문제?
def main():
    check = [False] * 1001
    num = int(input())

    for a in range(num, -1, -1):
        for b in range(num-a, -1, -1):
            for c in range(num-a-b, -1, -1):
                for d in range(num-a-b-c, -1, -1):
                    if a+b+c+d == num:
                        check[50*a+10*b+5*c+d] = True
    count = 0
    for i in range(0, num*50+1):
        if check[i]:
            count +=1
    print(count)
if __name__ == "__main__":
    main()