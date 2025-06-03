
#казино хохо
l = 1000
print("у вас ",l,"единиц  игровой валюты")
while True:
    print("введите свою ставку")
    f = int(input())
    while f <= 0 or f > l:
        print("введите число не превышающее колличество вашей игровой валюты,которое было бы больше 0")
        f = int(input())
    print("напишите число от 0 до 9 включительно")
    p = int(input())
    if p < 0 or p > 9:
        print("это число не подходит.введите число от 0 до 9 включительно")
    h = []
    for i in range(3):
        from random import randint
        m = randint(0, 9)
        h.append(m)
    print("автомат выдал числа ",h)
    d = h.count(p)
    if d == 0:
        print("вы проиграли")
        l = l - f
        if l == 0:
             print("вы банкрот:(")
             break
        else:
             print("у вас осталось ",l,"единиц игровой валюты")
    elif d == 1:
        print("вы выиграли")
        l = l + f
        print("теперь у вас",l,"единиц игровой валюты")
    elif d == 2:
        print("вы выиграли")
        l = l + f + f
        print("теперь у вас",l, "единиц игровой валюты")
    elif d == 3:
        print("ого!это джекпот!вы выиграли 100000000000")
        l = l + 100000000000
        print("теперь у вас", l, "единиц игровой валюты")
    print("если вы хотите закончить игру напишите'конец'")
    r = input()
    if r == "конец":
        break




n = int(input())
if n <= 18:
    print('привет')
else:
    print('здравствуй')
print("конец")



g = int(input())
if g%2 == 0:
    print("четное число")
else:
    print("нечетное число")

for i in range(4):
    print("я люблю котят")
print(i)

sum3 = 0
s4 = 0
for i in range(10):
    sum2= sum3 + 1
    s4 = sum + sum2

for i in range(1,11):
    if i%10 == 1 and i != 11:
        print(i,"манул")
    elif i%10 >= 2 and i%10 <= 4 and i !> 14 and i !< 12:
        print(i,"манула")
    elif i




