# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

S = int(input("Введите количество журавликов:  "))
# Пусть количество журавликов, которое сделали Петя и Сережа, равно x
# Тогда Катя сделала 2x журавликов

print('Петя сделал', S/6, 'журавликов')
print(' Сережа сделал', S/6, 'журавликов')
print('Маша сделала ', S/6*4, 'шт')
