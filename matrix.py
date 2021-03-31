try:
 N = int(input())
 if (N<=400)and(N>=4):
   a = [0] * N
   for i in range(N): a[i] = [0] * N
   x = 0
   y = 0
   counter_right = 1 # по дефолту выставляем 1, то бишь движение вправо
   counter_left = 0
   for i in range(N * N):
    a[y][x] = i + 1
    test = x + counter_right if counter_right else y + counter_left
    if test < 0 or test == N or a[y + counter_left][x + counter_right] != 0:
     counter_right, counter_left = -counter_left, counter_right
    x += counter_right
    y += counter_left
   for y in range(N): print(a[y])
 else:
  print('Some bullshit hapenned, plz give me int N in [4.400] n try agn')
except ValueError:
  print('Some bullshit hapenned, plz give me int N in [4.400] n try agn')
