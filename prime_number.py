n = input('自然数を入力してください。')
try: #ここではtry-except文を用いる。
    n = int(n)  # ユーザー入力を整数に変換
    if n <= 0:
        print('入力された数は自然数でない。')
    else:
        i = 2
        while i < n:
           if n%i == 0:
              print('nは素数でない。')
              break
           elif i < n:
              i += 1
        else: 
              print('nは素数である。')
except ValueError:
    print('入力された数は自然数でない。')