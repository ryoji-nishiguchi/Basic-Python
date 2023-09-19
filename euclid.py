a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

def god(c,d):
    while d!=0: #数式a=(a//b)*b+a%bにおいて、次の計算はaの値をbとしてa%bの値をbとして計算を繰り返す。
     c,d = c,c%d 
    print("2数a,bの最大公約数は",c) #処理終了後、aの値は数式a=(a//b)*b+a%bにおけるbの値と等しくなるため、最大公約数は処理完了後のaであると判断した。
if a >= b:
   c = a
   d = b

else: #上記のコマンドにおいてa,bを逆にすればよい。
  while a!=0:
        b,a = a,b%a
  print("2数a,bの最大公約数は",format(b))  
c = b
d = a
