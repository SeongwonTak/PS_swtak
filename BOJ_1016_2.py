check = [1]*1000001
start, end = map(int,input().split())
#start를 평행이동 하여 푼다.
#end-start+1개수 만큼 계산.
#어차피 divisibility만 체크하면 됨
#대신 가야하는 값은 end의 제곱근까지.
card = end-start+1
for i in range(2, end):
    if i * i > end:
        break
    pos_start = i * i - start % (i*i)
    if pos_start == i * i:
        pos_start = 0
    for j in range(pos_start, card, i * i):
        check[j] = 0

ans = 0
for i in range(card):
    ans += check[i]
print(ans)