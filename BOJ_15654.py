# N과 M 복습
# 대신 이번엔 수가 자유.
def main():
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list = sorted(num_list)
    visit = [False for _ in range(N)]
    result = []

    def solve(depth, num_list, visit, M):
        if depth == M:
            for i in range(0, len(result)):
                    print(result[i], end=" ")
            print()
            return

        for i in range(0, len(visit)):
            if not visit[i]:
                visit[i] = True
                result.append(num_list[i])
                solve(depth + 1, num_list, visit, M)
                visit[i] = False
                result.pop()

    solve(0, num_list, visit, M)

if __name__ == "__main__":
    main()