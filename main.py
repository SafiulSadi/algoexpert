n = int(input())
a = 0
b = 0
c = 0
while n > 0:
    arr = list(map(int, input().split()))
    a += arr[0]
    b += arr[1]
    c += arr[2]


    n -= 1

if a == 0 and b == 0 and c == 0:
    print("YES")
else:
    print("NO")
