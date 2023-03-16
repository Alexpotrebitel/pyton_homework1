# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

chislo=int(input('Введите шестизначное число'))
posledneechislo=chislo%10
vtoroechislo=int((chislo/10000)%10)
tretiechislo=int((chislo/1000)%10)
chetvertoechislo=int((chislo/100)%10)
pyatoetoechislo=int((chislo/10)%10)
pervoechislo=int(chislo/100000)

print(f'Сумма всех чисел равна{pervoechislo+vtoroechislo+tretiechislo+chetvertoechislo+pyatoetoechislo+posledneechislo}')
