# 수리공 항승
# https://www.acmicpc.net/problem/1449
# 간단한 Greedy 문제

def main():
    leaks, tape = map(int, input().split())
    leak_pt = list(map(int, input().split()))
    leak_pt = sorted(leak_pt)  # 정렬을 하고.
    fixing = [False] * leaks  # 고쳤나 여부를 확인하자.
    count_tape = 0

    for i in range(0, leaks): # 고친 칸을 확인하기 위함이다.
        if not fixing[i]: # 고치지 못했다면 고치는 과정 진행
            st_pt = leak_pt[i] - 0.5
            end_pt = st_pt + tape
            count_tape += 1

            for j in range(0, leaks):
                if leak_pt[j] < end_pt:
                    fixing[j] = True

    print(count_tape)

if __name__ == '__main__':
    main()