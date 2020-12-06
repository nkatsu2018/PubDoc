# coding: utf-8

# クラス定義1：__str__の定義なし
class C1:
	def __init__(self):
		self.a = 1
		self.b = 2
		self.c = 3

x1 = C1()
print( 'str(x1):',str(x1) )

# クラス定義2：__str__の定義あり
class C2:
	def __init__(self):
		self.a = 1
		self.b = 2
		self.c = 3
	def __str__(self):
		r = 'a='+str(self.a)+',b='+str(self.b)+',c='+str(self.c)
		return r

x2 = C2()
print( 'str(x2):',str(x2) )
