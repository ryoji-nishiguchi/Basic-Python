a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
def god(a,b): #(a,b)の最大公約数を求める関数を定義
 if a >= b:
    if b == 0:
     return a
    else:
     return god(b,a%b) #bの値が0になるまで何度も自分自身を呼び出す。
 else:
   return god(b,a)

def god2(a,b):
 if god(a,b)==1:
    return True
 else:
  return False
print('整数(a,b)の最大公約数は{}。'.format(god(a,b)))
print('整数(a,b)の最大公約数が互いに素である命題は{}である。' .format(god2(a,b)))
