
#.(dot)(.)

import re
pattern = r'e.t'
text="e@t eaat emt ett emmt emt Emt hkjht"

res=re.findall(pattern,text)

print(res)

#['e@t', 'emt', 'ett', 'emt']



# ^ cap starting weith 91 or not
import re
pattern = r'^(91)'
text="91545458"

res=re.findall(pattern,text)

print(res)



#$ ending with this or not 
import re
pattern = r'0$'
text="9876544789065030"

res=re.findall(pattern,text)

print(res)



#[* ,+  ]+means one or more occures ,* means 0 or more occurence  
#*
import re
pattern = r'to*'
text="to toooo tooo tojkj thjijjk t "

res=re.findall(pattern,text)

print(res)
#['to', 'toooo', 'tooo', 'to', 't', 't']



#+
pattern = r'to+'
text="to toooo tooo tojkj thjijjk to "

res=re.findall(pattern,text)

print(res)
#['to', 'toooo', 'tooo', 'to', 'to']





#?+++++++++++++++++++++++++++++learn????


#||||  this orthat#learnnnnn


pattern = r'91|0'
text="91056780 "

res=re.findall(pattern,text)

print(res)




pattern = r'[aeiouAEIOU]'#[check whaether the value ]
text="codegnan programming"

res=re.findall(pattern,text)

print(res)

#['o', 'e', 'a', 'o', 'a', 'i']
