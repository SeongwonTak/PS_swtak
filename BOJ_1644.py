# 소수의 연속 합
# Si-Sj 의 형태로 표현하면 된다.
def prime_judge(num):
    judge = True
    for i in range(2, int(num ** (0.5))+1):
        if num % i == 0:
            judge = False
            break
    return judge

def prime_list(num):
    list = []
    for i in range(2 , num):
        if prime_judge(i) == True:
            list.append(i)
    return list

def main():
    num = int(input())
    primes = prime_list(num)  # 소수 행 받아옴

    count = 0
    if prime_judge(num) == True:
        count += 1

    if len(primes) > 1:
        start_pos = 0
        end_pos = 0
        sum = primes[0]
        while end_pos < len(primes):
            if sum == num:
                count += 1
                end_pos += 1
                if end_pos < len(primes):
                    sum += primes[end_pos]
            elif sum > num:
                sum -= primes[start_pos]
                start_pos += 1
            elif sum < num:
                end_pos += 1
                if end_pos < len(primes):
                    sum += primes[end_pos]

    if num != 1:
        print(count)
    else :
        print(0)
if __name__ == "__main__":
    main()