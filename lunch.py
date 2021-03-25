import random

list = ['インドカレー', '蘭州ラーメン', '松屋', '餃子の王将', '桜', '海鮮丼']
num = len(list)-1
randomnum = random.randint(0, num)
print(list[randomnum])