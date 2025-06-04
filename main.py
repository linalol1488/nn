from random import *
r = randint(1,10)
g = 3
print("как вы думаете,какое число загадано?")
h = int(input())
while h < 1 or h > 10:
    print("введите число от 1 до 10")
    h = int(input())
while True:
    if r > h:
        print("загаданное число больше")
        g = g - 1
        if g == 0:
            print("у вас осталось 0 попыток,вы проиграли(")
            break
        else:
            print("у вас осталось ", g, " попыток")
            print("как вы думаете,какое число загадано?")
            h = int(input())
    elif r < h:
        print("загаданное число меньше")
        g = g - 1
        if g == 0:
            print("у вас осталось 0 попыток,вы проиграли(")
            break
        else:
            print("у вас осталось ", g, " попыток")
            print("как вы думаете,какое число загадано?")
            h = int(input())
    elif r == h:
        print("вы выиграли!онец игры")
        break
