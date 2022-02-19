'''63)	(Д.Ф. Муфаззалов) В файле записана последовательность натуральных чисел. Из этой последова-тельности нужно
выбрать четыре числа так, чтобы их сумма при делении на число 9 не давала оста-ток ноль и была наименьшей. Какова сумма
этой четверки чисел?'''
from itertools import *
max=100000000
s1=[]
f=open('27-63a.txt','r')
n=int(f.readline())
for i in range(n):
    s1.append(int(f.readline()))
#s1=
#s1=[0,1,2,3,4,5,6,7,8]
for i in combinations(s1,4):
    #print(i,sum(i))
    if sum(i)%9!=0 and sum(i)<max:
        max=sum(i)
print(max)
#print(list(combinations(s1,4))) #сочетания без повторений

#print(s.count('2'))

