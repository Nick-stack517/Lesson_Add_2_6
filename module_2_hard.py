import random

numbers = []

for i in range(3, 21):  # Заполнил список от 3 до 20
    numbers.append(i)


def dice():
    dice_out = random.choice(numbers)
    return dice_out


num = dice()
# num = int(input('Введите чилсло: '))
password = []
result = []

for i in range(1, num):
    for k in range(i + 1, num):
        if num % (i + k) == 0:
            password.append([i, k])
            result.append(str(i))
            result.append(str(k))

print('Подбор пароля для числа: ', num)
print('Подходящие пары чисел:')
print(password)
print()
print('Ответ:')
print(''.join(result))
