# N제곱 계산

def matrix_prod(b):
    a = [6, -4, 1, 0]
    ans = [1, 0, 0, 1]
    while b != 0:
        if b % 2 == 1:
            new_ans = [0, 0, 0, 0]
            new_ans[0] = (a[0] * ans[0] + a[1] * ans[2]) % 1000
            new_ans[1] = (a[0] * ans[1] + a[1] * ans[3]) % 1000
            new_ans[2] = (a[2] * ans[0] + a[3] * ans[2]) % 1000
            new_ans[3] = (a[2] * ans[1] + a[3] * ans[3]) % 1000
            ans[0] = new_ans[0]
            ans[1] = new_ans[1]
            ans[2] = new_ans[2]
            ans[3] = new_ans[3]

        new_a = [0, 0, 0, 0]
        new_a[0] = (a[0] * a[0] + a[1] * a[2]) % 1000
        new_a[1] = (a[0] * a[1] + a[1] * a[3]) % 1000
        new_a[2] = (a[2] * a[0] + a[3] * a[2]) % 1000
        new_a[3] = (a[2] * a[1] + a[3] * a[3]) % 1000

        a[0] = new_a[0]
        a[1] = new_a[1]
        a[2] = new_a[2]
        a[3] = new_a[3]

        b = b // 2

    return ans[0], ans[1], ans[2], ans[3]

def solve(num):
    x = 28
    y = 6
    if num == 1:
        return y - 1
    elif num == 2:
        return x - 1
    else:
        matrix = [0, 0, 0, 0]
        matrix[0], matrix[1], matrix[2], matrix[3] = matrix_prod(num-2)
        answer = matrix[0] * x + matrix[1] * y
        return (answer - 1) % 1000

def main():
    case = int(input())
    for i in range(0, case):
        num = int(input())

        ans = solve(num)
        if ans // 100 != 0:
            new_ans = str(ans)
        elif ans // 10 != 0:
            new_ans = "0"+str(ans)
        else:
            new_ans = "00"+str(ans)
        print("Case #%d: %s" %(i+1, new_ans))

if __name__ == "__main__":
    main()