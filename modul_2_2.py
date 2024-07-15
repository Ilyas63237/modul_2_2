first = int(input('Введите число: '))
second = int(input('Введите следующее число: '))
third = int(input('Введите третье число: '))
if first == second == third :
    print('3')
elif first == second or second == third or first == third :
    print('2')
else:
    print('0')