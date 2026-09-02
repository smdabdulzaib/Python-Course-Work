#Regular Expression (Regex) in Python

#Regular Expression is a pattern used to search, match, extract, or replace text in a string.


#match: check whaetheer string starting with my pattern or not:

#search stop when found first letter like 2 it found it stop and give found output
#findall:all output 
#find iter finds the iters
#full match =for validation extract needto match
#splitt: splutt accord to ( )splitt multiple patterms
#(sub)
# (used for replacin purposeit replaces number with * )gnerally if we need replace we usereplace for each so we use this





#match:
import re
pattern=r'[0-9]'
text='codegnan'

res=re.match(pattern,text)

print(res.group() if res else "Pattern not found")



#search stop when found first letter like 2 it found it stop and give found output

import re
pattern=r'[0-9]'
text='codegnan2026'

res=re.search(pattern,text)

print(res.group() if res else "Pattern not found")

#findall:all output 

pattern=r'[0-9]'
text='codegnan 2026 python version 3.14'

res=re.findall(pattern,text)
print(res)

#print(res.group() if res else "Pattern not found")


pattern=r'[0-9]'
text='codegnan 2026 python version 3.14'

res=re.findall(pattern,text)
print(res)



#find iter finds the iters

pattern=r'[0-9]'
text='codegnan 2026 python version 3.14'

res=re.finditer(pattern,text)#lazy loder we use for loop
for i in res:
    print(i.group(),i.start())
#print(res)
  
  #full match =for validation extract needto match
pattern=r'[0-9]{10}'
text='987657898765'

res=re.fullmatch(pattern,text)
print(res)


#full match used them to  full match




#splitt: splutt accord to ( )splitt multiple patterms
S
import re 
pattern = r'[,(#]'
text="java,python(html#css"

res=re.split(pattern,text)
print(res)




#(sub) #re.sub(pattern, replacement, text)



# (used for replacin purposeit replaces number with * )gnerally if we need replace we usereplace for each so we use this


pattern=r'[a-z]'
text="python version 3.14, batch-63"

res=re.sub(pattern,'*',text)

print(res)