print("Hello world!")
print('*' * 50)
for i in range(1, 50):
    if i % 2 == 0:
        print('Мне нравится программировать!')
        number = int(input('Введите число'))
        print(f'Результат: {i * number}')
    else:
        continue
