a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

if a >= b:
    while b!=0:  #数式a=(a//b)*b+a%bにおいて、次の計算はaの値をbとしてa%bの値をbとして計算を繰り返す。
       a,b = b,a%b  
    print("2数a,bの最大公約数は",a) #処理終了後、aの値は数式a=(a//b)*b+a%bにおけるbの値と等しくなるため、最大公約数は処理完了後のaであると判断した。


else: #上記のコマンドにおいてa,bを逆にすればよい。
  while a!=0:
        b,a = a,b%a
  print("2数a,bの最大公約数は",format(b))  
