# ГНОМЬЯ СОРТИРОВКА
print('ВАС ПРИВЕТСТВУЕТ ПРОГРАММА СОРТИРОВКИ ЧИСЕЛ')
print()
f = 1                                                       
# условие для дальнейшей работы программы
while f == 1:
# запрос размерности списка у пользователя с организацией исключений
    T = True
    while  T == True:
        print("Сколько чисел вы хотите ввести для сортировки?")
        try:
            n = input()
            n = int(n)
            T = False
        except:
            print(
''' ЭТО НЕ ЧИСЛО!!!

Попробуйте ещё раз все заново.'''
                )
    a = []
    print('Вводите числа')
# заполнение списка пользователем
    P = True
    while n > 0:
        P = True
        while P == True:
            try:
                x = input()
                x = int(x)
            except:
                print(
'''ЭТО НЕ ЧИСЛО!

Попроьуй написаь ещё раз то число которое не вызвало эту оштбку'''
                    )
                P = False
            a.append(x)
            if P == True:
                P=False
                n = n - 1
            else:
                pass
# измерение длины получившегося списка
    g = len(a)

# непосредственно алгоритм гномьей сортировки через фуекцию Gnom_Sort()
    def Gnom_Sort(a):
        i = 1
        j = 2
        E = True
        while E == True:
            print('''Если вы хотите начать сортировку заданных чисел по возрастанию нажмите "1"
Если же вы хотите отсортировать последовательность по убыванию нажмите "0"''')
            vvod = input()
            vvod = int(vvod)
            if vvod == 1:
# организация сравнения элемента списка с предыдущим
                while i < g:
# если элемент больше предыдущего, происходит переход к следующим двум элементам
                    if a[i-1] <= a[i]:
                        i = j
                        j = j + 1
# если элемент меньше предыдущего, происходит перестановка этих элементов в списке
                    else:
                        a[i-1], a[i] = a[i], a[i-1]
                        i = i - 1
                        if i == 0:
                            i = j
                            j = j + 1
                    E = False
                return(a)
            else:
                if(vvod == 0 ) and (vvod != 1):
                    while i < g:
# если элемент больше предыдущего, происходит переход к следующим двум элементам
                        if a[i-1] >= a[i]:
                            i = j
                            j = j + 1
# если элемент меньше предыдущего, происходит перестановка этих элементов в списке
                        else:
                            a[i-1], a[i] = a[i], a[i-1]
                            i = i - 1
                            if i == 0:
                                i = j
                                j = j + 1
                    return(a)
                else:
# Указание на тупость пользователя
                    print('Внимательно читайте инструкию!')
            E = False                
    print(Gnom_Sort(a))
# запрос повторного ввода
    print("Вы хотите еще раз запустить программу? (y/n)")
    h = input()                                             
    if h == 'y':
        pass
    elif h == 'n':
        f = 0
# обработка исключения (не введено ни y, ни n)
    elif (h != 'y') and (h != 'n'):
        print("Вы не слушаетесь программу и она обиделась =(")
       
input()
