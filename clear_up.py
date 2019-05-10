# ecoding=utf-8
#这个程序将获取到的QQ群聊天记录中的数字删除，避免日期干扰实验结果！
ifn = r"D:\\搏一搏，单车变摩托.txt"#原始文本
ofn = r"D:\\output.txt"#整理好的文本

infile = open(ifn, 'r',encoding="utf-8")#统一编码格式为utf-8
outfile = open(ofn, 'w+',encoding='utf-8')
txt =""
for eachline in infile.readlines():
    lines = filter(lambda ch: ch not in ' \t1234567890', eachline)
    strr = list(lines)
    txt =''.join(strr)
    txt =str(txt)
    outfile.write(txt)
infile.close
outfile.close
