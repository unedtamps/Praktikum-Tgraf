n = int(input())
vc = list(map(int, input().split()))
lg = [1] * n

for i in range(1, n):
    for j in range(i):
        if vc[i] > vc[j] and lg[i] <= lg[j]:
            lg[i] = 1 + lg[j]

pr = (0, 0)
res = []


for i in range(n):
    if lg[i] > pr[1]:
        pr = (i, lg[i])

res.append(pr[0])

for i in range(pr[0] - 1, -1, -1):
    if lg[res[-1]] - 1 == lg[i]:
        res.append(i)

print("urutan:", end=" ")
for i in reversed(res):
    print(vc[i], end=" ")

print("\nhasil:", pr[1])