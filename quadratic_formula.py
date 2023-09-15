a = 8
b = -6
c = -35

import math
# TODO
if (b**2 - 4*a*c) >= 0:
 x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
 x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
 print(x1,x2)

else:
  x3 = (-b / (2*a)) + (math.sqrt(4*a*c - b**2)) / (2*a)
  x4 = (-b / (2*a)) - (math.sqrt(4*a*c - b**2)) / (2*a)
  print(str(x3) + "j",str(x4) + "j")

