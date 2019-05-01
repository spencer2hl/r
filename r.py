import random
start = input('请决定随机数字范围开始值')
end = input('请决定随机数字范围结束值')
start = int(start)
end = int(end)
r = random.randint(start, end) # 包含了1和100
count = 0
while True:
	count = count + 1 #count += 1 快写法
	num = input('请猜数字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这是你猜的第', count, '次')
