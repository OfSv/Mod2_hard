# функция возвращает пароль для введённого числа k

def password(k):
    pw = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            ij = i + j
            if k % ij == 0:
                pw += str(i)
                pw += str(j)
    return pw


print("Введите число от 3 до 20: ")
n = int(input())
result = password(n)
print('Пароль: ', result)
