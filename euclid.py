a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
def god(a,b): #(a,b)の最大公約数を求める関数を定義
 if a >= b:
    c = a
    d = b
 else:
    d = a
    c = b
    while d>0:
       (c,d) = (d,c%d)
    return c

print('整数(a,b)の最大公約数は{}である。'.format(god(a,b)))

if (god(a,b) == 1) == True:
   print('整数(a,b)は互いに素である。')
else:
   print('整数(a,b)の最大公約数は{}であり、互いに素でない。' .format(god(a,b)) )