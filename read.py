data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 是用來求餘數
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d)
print('每筆留言平均長度為', sum_len / len(data))

# data 中的資料一筆一筆拿出來，每一筆資料為 d
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])


# 文字計數
wc = {} #word_count
for d in data:
	words = d.split() #split 預設值為空格
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的 key 進 wc 字典

for word in wc:   # 每一個 word 為 key
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你要查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('這個字沒出現過')
print('感謝您使用本查詢功能')




# #list comprehension 清單快寫法
# good = [1 for d in data if 'good' in d]
# print(good)
# #第一個 d 的地方為運算 ,若改為1, 則 good 清單裡有 16 萬個 1
# bad = ['bad' in d for d in data] # 'bad' in d 為運算(是非題)
# print(bad)

# bad = []
# for d in data:
# 	bad.append('bad' in d)
