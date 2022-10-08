import json
f = open("E:/abc.txt","r") 
lines = f.readlines()      #读取全部内容 ，并以列表方式返回
a = []
for line in lines:
    a.append(json.loads(line))

with open("E:/vtr_vte_seq_6TR6TE_zy.json", 'w') as f:
    json.dump(a, f)
