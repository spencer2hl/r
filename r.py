import random

r = random.randint(1, 100) # 包含了1和100
while True:
	num = input('请猜数字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
