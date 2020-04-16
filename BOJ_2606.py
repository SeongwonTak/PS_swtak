# 바이러스
# dfs 로 풀어보았다.

def search(start, com_conn, virus_com, com):
    for i in range(0, com):  # 0번부터 com까지 돈다
        if com_conn[start][i] == 1 and virus_com[i] == 0:
            # 연결이 안되어 있는 최초의 애를 지정해주는 작업을 한다.
            virus_com[i] = 1
            new = i  # 새로 탐색할 시작 거점 결정
            search(new, com_conn, virus_com, com)
    return virus_com

def main():
    com = int(input())
    nodes = int(input())
    com_conn = [[0] * com for i in range(com)]
    for i in range(nodes):  # 연결 상태 입력
        x, y = map(int, input().split())
        com_conn[x - 1][y - 1] = 1
        com_conn[y - 1][x - 1] = 1

    virus_com = [0] * com
    virus_com[0] = 1  # 1번 컴퓨터 감염!

    ans_com = search(0, com_conn, virus_com, com) # dfs
    print(sum(ans_com)-1)  # 감염자는 모두 1이니 그걸 더한다.
    # 문제를 잘 읽자 1번 빼고 답해야 한다.

if __name__ == '__main__':
    main()
