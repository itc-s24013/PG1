import collections

data = 'すもももももももものうち'
count_dic = {}
for v in data:
    if v in count_dic:
        count_dic[v] += 1
    else:
        count_dic[v] = 1
print(count_dic)

count_dic = collections.defaultdict(int)
for v in data:
    count_dic[v] += 1
print(count_dic)

count_dic = collections.defaultdict(list)
for v in data:
    count_dic[v].append(v)
print(count_dic)

counter = collections.Counter(data)
print(counter)

print(counter['す'])
print(counter['ぽ'])

CharCount = collections.namedtuple('CharCount', ['char', 'count'])
mo = CharCount('も', 8)
print(mo)
print(mo.char, mo.count)


res_dict = collections.defaultdict(list)
print(res_dict)
for ch, cnt in counter.items(): #辞書型
    res_dict[cnt].append(ch) 
    print(res_dict)
    print(f'ch:{ch}')
    print(f'cnt:{cnt}')
print(res_dict[1])
