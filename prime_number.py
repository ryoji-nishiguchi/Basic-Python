a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# aが素数であることを調べる。
def judging_prime(c):
    if c <= 1:
     print(c,"は素数ではありません。")
    else:
     prime_c = True
     for i in range(1,c //2):
      if c % (i+1) == 0:
        prime_c = False
      break  
     if prime_c == True:
        print(c, "は素数です")
     else:
        print(c, "は素数ではありません")
    
judging_prime(a)
judging_prime(b)

