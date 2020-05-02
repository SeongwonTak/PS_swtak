# 부분 수열의 합
# https://www.acmicpc.net/problem/1182
def sum_check(result, sum):
    check_sum = 0
    for i in range(0, len(result)):
        check_sum += result[i]
    if check_sum == sum:
        return True
    else:
        return False

num, sum = map(int, input().split())
num_list = list(map(int, input().split()))
visited = [0] * num
count = 0
result = []
def dfs(depth, L, num, sum):
    global count

    if depth == num:
        return

    for i in range(L, num):
        visited[i] = True
        L = i+1
        result.append(num_list[i])

        if sum_check(result, sum):
            count += 1

        dfs(depth+1, L, num, sum)
        visited[i] = False
        result.pop()

dfs(0, 0, num, sum)
print(count)
