# 부분 수열의 합
# https://www.acmicpc.net/problem/1182
def dfs(depth, num, sum):
    pass

def main():
    num, sum = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list.append(0) #이게 바로 합이 맞을때마다 1이 올라갈 변수다. 맨 마지막 칸이다.

    dfs(0, num, sum)


if __name__ == "__main__":
    main()