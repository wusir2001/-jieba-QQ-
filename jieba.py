import jieba
txt = open("D:\\output.txt","r",encoding='utf-8').read()
hhh = open("D:\\list.txt", 'w+',encoding='utf-8')
words = jieba.lcut(txt)#进行jieba分词
counts={}
for word in words:
    if len(word) <=1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(150):#打印出出现频率前150的词汇
    word,count=items[i]
    hhh.write("{0:<5}{1:>5}\n".format(word,count))
