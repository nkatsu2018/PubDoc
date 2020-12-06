# coding: utf-8

# クラス名の文字列を取得
def k(o): return o.__name__

# クラス階層の出力
def getSubclasses(cls,n=0):
	sc = sorted(type.__subclasses__(cls),key=k)
	for scls in sc:
		print('    '*n+str(scls))
		getSubclasses(scls,n+1)
#
if __name__ == '__main__':
	getSubclasses(object)
