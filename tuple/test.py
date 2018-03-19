'''算法重要性
通过一个小时候常听到的高斯求和故事举例，使用恰当的算法，可以明显优化程序，减少运算时间
'''
import time

def sum1(n):
	'''通过 for循环求和'''
	sum = 0
	for i in range(n+1):
		sum = sum + i
	return sum

def sum2(n):
	'''通过等差数列求和'''
	return (1+n)*n/2

if __name__ == '__main__':
	start = time.time()
	print(sum2(99999999))
	end = time.time()
	print(end-start)
