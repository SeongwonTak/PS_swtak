# https://www.acmicpc.net/problem/1912
# 또 DP 같긴 한데.

def main():
    num = int(input())
    num_list = list(map(int, input().split()))
    max_list = []
    for i in range(0, num):
        if i == 0:
            max_list.append(num_list[i])
        else:
            if max_list[i-1]+num_list[i] > num_list[i]:
                max_list.append(max_list[i-1] + num_list[i])
            else:
                max_list.append(num_list[i])

    print(max(max_list))

if __name__ == "__main__":
    main()