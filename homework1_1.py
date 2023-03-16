# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5

# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1

chislo=int(input('Введите трехзначное число'))
posledneechislo=chislo%10
pochticislo=chislo/10
vtoroechislo=pochticislo%10
pervoechislo=chislo/100
print(f'Сумма всех чисел равна{int(posledneechislo+vtoroechislo+pervoechislo)}')


