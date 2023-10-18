import math
n = input('自然数を入力してください.')
def judge_prime(x):
    if not x.isdigit():  # nが整数であることの真偽
        return '入力された数は自然数でありません。'
    x = int(x)  # 文字列を整数に変換
    if x <= 0:
        return '入力された数は自然数でありません。'
    else:
        i = 2
        while i < x:
            if x % i == 0:
                return 'nは素数でない。'
            else:
                i += 1
        else:
            return 'nは素数である。'

print(judge_prime(n))
