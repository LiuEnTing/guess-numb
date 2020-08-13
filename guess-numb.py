import random

start = input('請決定隨機數字開始範圍:')
end = input('請決定隨機數字結束範圍')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1
	numb = input('請猜數字')
	numb = int(numb)
	if numb == r:
		print('你猜對了 很棒~')
		print('這是第', count,'次，很棒')
		break
	elif numb < r:
		print('再大一點 快猜到了')
	elif numb > r:
		print('太大再小一點點')

	print('這是第', count,'次，再加油')