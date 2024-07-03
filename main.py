# young physicist
# n = int(input())
# a = 0
# b = 0
# c = 0
# while n > 0:
#     arr = list(map(int, input().split()))
#     a += arr[0]
#     b += arr[1]
#     c += arr[2]
#
#
#     n -= 1
#
# if a == 0 and b == 0 and c == 0:
#     print("YES")
# else:
#     print("NO")
    #
    # # beautiful matrix
    # arr = []
    # for i in range(5):
    #     brr = list(map(int, input().split()))
    #     arr.append(brr)
    # #     print(brr)
    # # print(arr)
    # x = 0
    # y = 0
    # for i in range(5):
    #     for j in range(5):
    #         if arr[i][j] == 1:
    #             x = i
    #             y = j
    # # print(f"x: {x} Y:{y}")
    # print(f"{abs(2 - x) + abs(2 - y)}")

# abc = {1:5, 2:6}
# print(abc[1])
#
# arr = [1, 2, 3]
#
# n = int(input())
# drr = {}
#
# while n > 0:
#
#     arr = list(input().split())
#
#     print(arr)
#     print(drr)
#     print("drr")
#
#     if arr[0] in drr.keys():
#         print("yeag")
#         an = drr[arr[0]] + int(arr[1])
#         drr.pop(arr[0])
#         drr[arr[0]] = an
#         print("drr[arr[0]]")
#         print(drr[arr[0]])
#     else:
#         drr[arr[0]] = int(arr[1])
#         print(drr)
#     print(drr)
#     n -= 1
#
# print(drr)
# vrr = []
# for k, v in drr.items():
#     krr = []
#     krr.append(k)
#     krr.append(v)
#     vrr.append(krr)
# crr = list(drr)
# print(crr)
# print(vrr)
# ind = 0
# max = 0
# for i in range(len(vrr)):
#     if vrr[i][1] > max:
#         max = vrr[i][1]
#         ind = i
#         print(max)
#     else:
#         pass
# print(vrr[ind][0])
#
#
#
#
#
#
# # 3
# # mike 3
# # andrew 5
# # mike 2
#
#
# n, t = map(int, input().split())
# ax = input()
# x = [i for i in ax]
# print(x)
# q = []
# for i in range(t):
#     for j in range(len(x)-1):
#         if x[j] == "B" and x[j+1] == "G":
#             x[j] = "G"
#             x[j+1] = "B"
#             print(x)
#             q.append(x[j])
#
#         else:
#             q.append(x[j])
#             pass
# print("Q")
# print(q)
# ans = ""
# for i in x:
#     ans += i
# print(ans.strip())
#
# # 52 A. Bus to Udayland
#
# n = int(input())
# arr = []
#
# while n > 0:
#     brr = input().split("|")
#     print(brr)
#     arr.append(brr)
#     n -= 1
# print(arr)
# a = (0, 0)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] == "OO":
#             a = (i, j)
#             arr[i][j] = "++"
#             break
#         else:
#             continue
# print(a)
# print(arr)
# print(len(arr[0]))
#
#
# 53 A. Brain's Photos
#
# n, m = map(int, input().split())
# arr = []
# sett = set()
# while n > 0:
#     arr = list(map(str, input().split()))
#     # print(arr)
#     for i in arr:
#         sett.add(i)
#     n -= 1
# # print(arr)
# # print(sett)
# flag = "#Black&White"
# for i in sett:
#     if i == "C" or i == "M" or i == "Y":
#         flag = "#Color"
#         break
# print(flag)

# 53 A. Hulk

n = int(input())
x = ""
for i in range(1, n):
    if i % 2 == 0:
        x += "I love that "
    else:
        x += "I hate that "
if n % 2 == 0:
    x += "I love it"
else:
    x += "I hate it"
print(x)

















