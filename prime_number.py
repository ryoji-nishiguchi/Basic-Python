a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# aが素数であることを調べる。

if a <= 1:
    print(a,"は素数ではありません。")
else:
 prime_a = True
 for i in range(1,a //2):
    if a % (i+1) == 0:
      prime_a = False
      break  
if prime_a == True:
        print(a, "は素数です")
else:
        print(a, "は素数ではありません")

if b <= 1:
    print(b,"は素数ではありません。")
else:
 prime_b = True
 for i in range(1,b //2):
    if b % (i + 1) == 0:
      prime_b = False 
 if prime_b == True:
        print(b, "は素数です")
 else:
        print(b, "は素数ではありません")