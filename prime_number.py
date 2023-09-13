a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO

if a <= 1:
    print(a,"は素数ではありません。")
else:
 prime_a = True
 for i in range(1,a //2):
    if a % (i + 1) == 0:
      prime_a = False
      break  
    if prime_a == True:
        print(a, "は素数です")
        break
    else:
        print(a, "は素数ではありません")
        break