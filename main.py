a = [4, 5, 6, 7, 8, 1]
print(a[-1])

print(a[-1])
for i in range(3):
    print(i)
print(a)

count1 = 0
count2 = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])
        count2 += 1
    if a[i] % 2 == 1:
        count1 += a[i]
print(a)
print(count1)
print(count2)


s = [5, 4, 5, 3, 2, 5, 5, 4, 5, 4, 3, 5,]
j = 0
for i in range(len(s)):
    j = j + s[i]
j = j/len(s)
print(j)

