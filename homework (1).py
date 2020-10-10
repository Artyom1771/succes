#номер1
x=int(input())
y=int(input())
def division():
    try:
        result=x/y
    except ZeroDivisionError:
        print('Деление на ноль')
    print(result)
division()



#номер2
def person(name,surname,town,date,email,phone):
    return ' '.join([name,surname,town,date,email,phone])
print (person(name='Артём',surname='Титов',date='2004',town='Chita',email='@',phone='89001111111'))

#номер3
def my_func(arg1,arg2,arg3):
    if arg1>arg2 and arg2<arg3:
        print(arg1+arg3)
    if arg1 > arg3 and arg2 > arg3:
        print(arg1 +arg2)
    if arg1<arg2 and arg3>arg1:
        print(arg3+arg2)
my_func(5,2,3)


#номер4
def my_func(x,y):
    result=x**y
    print(result)
my_func(1,-2)

#номер 6
def int_func(word):
    print(word)
int_func('bts'.title())
def int_f(str):
    print(str)
int_f(input('Введите строку').title())


