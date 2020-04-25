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

    for i in range(1, len(primes)):
        primes[i] = primes[i] + primes[i-1]

    count = 0
    if prime_judge(num) == True:
        count += 1

    if len(primes) > 1:
        for i in range(len(primes)-1, 0, -1):
            for j in range(i, -1, -1):
                if primes[i] - primes[j] == num:
                    count += 1

    for i in range(0, len(primes)):
        if primes[i] == num and num != 2:
            count += 1

    print(count)
if __name__ == "__main__":
    main()
