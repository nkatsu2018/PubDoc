# coding: utf-8
import time
# フィボナッチ数を算出する関数
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

# F0～F19 までのフィボナッチ数列
print('F0-F19',[fib(n) for n in range(20)])

# F0～F35 までのフィボナッチ数列
t1 = time.time()
print('\nF0-F35',[fib(n) for n in range(36)])
t2 = time.time()
print('計算時間:',t2-t1,'(sec)')
