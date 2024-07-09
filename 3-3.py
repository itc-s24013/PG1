my_list = [0, 1, 4, 9, 16, 25, 36]
for i in my_list:
    if i % 2 == 0:
        print(i)

my_list = ['tokyo', 'osaka', 'fukuoka', 'aichi', 'kyoto', 'chiba', 'saitama', 'gunma']
my_list_6 = []
for s in my_list: #my_listの要素の数繰り返す
    if len(s) >= 6: #6文字以上の要素の場合
        my_list_6.append(s) #my_list_6に要素を追加する
print(my_list_6)
