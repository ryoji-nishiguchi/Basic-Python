from math import sin,pi
h = (pi/2)/100 #問題文に基づいて考えた。 
k = 1
s = 0 #初期状態を定義 
while k <= 100:
 s += (h/2)*(sin((k-1)*h)+sin(k*h)) #問題文にあったaの値は0であるから省略した。
 k = k + 1
print(s)  
