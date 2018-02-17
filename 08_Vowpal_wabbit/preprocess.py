import sys
from tqdm import tqdm

file_name_input=sys.argv[1]
file_name_output=sys.argv[2]

tokens=['javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift']
table = str.maketrans(':|', '  ')

f = open(file_name_input,'r')
f_out = open(file_name_output,'w')
pbar = tqdm()
strnum=0
for line_str in f:
    pbar.update(1)
    if line_str.count('\t')!=1: continue#одна табуляция
    ind=line_str.find('\t')#находим делитель колонок
    
    filtr_tokens=list(filter(lambda val: val in tokens, line_str[ind+1:].rstrip().split(' ')))#есть ли  теги в нужных токенах
    if len(filtr_tokens)!=1: continue#должен быть только один
        
    textq=line_str[:ind-1].translate(table).lstrip()#замена символов в вопросе
    if(len(textq)==0): continue#пустая строка нам не нужна
    f_out.write(str(tokens.index(filtr_tokens[0])+1) +' | ' + textq + '\n')#пишем в файл по формату кволика
    strnum+=1
        

pbar.close()
print('Количество записей: ',strnum)
print('Должно быть       :  4389054')

f.close()
f_out.close()
