import re

data = r'''
gkphk=\'\';
xshgxzgf=\';whi\';
sdgvd=\'0,y\';
xrswtvc=\' ws\';
sjoapzt=\'twax\';
mfecyrm=\'ngth>\';
fhkmqp=\'=ya\';
zxtsiqh=\'.le\';
oojjaqhf=\'le(ya\';
ztghjl=\'+=yao\';
krnhojui=\'uhc.\';
jlewfxk=\'odu\';
smljrb=\'gth-\';
ddytxnxk=\'doe\';
oueqbm=\'uhc)\';
fqwyzxgz=\'0){yu\';
fceskr=\'{yun\';
kmqzsjw=\'aoduh\';
qhrqfw=\'1);\';
vcymzsr=\'s;};\';
jvdcvb=\'hc.su\';
gohyw=\'oes\';
exfrbokx=\'(yaod\';
bhmtsl=\'aod\';
kwnwoex=\'ring(\';
fchzbi=\'funct\';
hsqxcx=\'nkl\';
nagmbm=\'}re\';
imxawkuu=\'nkld\';
mdxqji=\'duh\';
chgduhrd=\'duhc\';
mbptj=\'oduhc\';
spzjhwq=\'harAt\';
alxtxqo=\'turn\';
xujipt=\'ap(y\';
cocofnhc=\'es=""\';
mefcuf=\'c.c\';
tddbds=\'bst\';
apebh=\'lengt\';
sxgununp=\'kldo\';
mgeztzln=\'h-1\';
hkcoctuy=\' yu\';
vtfon=\');yao\';
crldyth=\'ion\';
xvuzqi=\'c.len\'; '''

import re

# Initialize an empty dictionary
result_dict = {}

# Split the data into lines
lines = data.strip().split('\n')

# Process each line to extract key-value pairs and add them to the dictionary
for line in lines:
    key, value = line.split('=', 1)
    key = key.strip()
    value = value.strip().strip("'")
    new_value = ""
    counter = 0
    for char in value:
        if char == "'" or char == "\\":
            counter += 1
            if counter == 4:
                break
        else:
            new_value += char
    result_dict[key] = new_value

initial_text = "fchzbi+crldyth+xrswtvc+sjoapzt+xujipt+bhmtsl+oueqbm+fceskr+sxgununp+cocofnhc+xshgxzgf+oojjaqhf+mbptj+zxtsiqh+mfecyrm+fqwyzxgz+imxawkuu+gohyw+ztghjl+mdxqji+mefcuf+spzjhwq+exfrbokx+krnhojui+apebh+mgeztzln+vtfon+chgduhrd+fhkmqp+jlewfxk+jvdcvb+tddbds+kwnwoex+sdgvd+kmqzsjw+xvuzqi+smljrb+qhrqfw+nagmbm+alxtxqo+hkcoctuy+hsqxcx+ddytxnxk+vcymzsr;"

initial_text = initial_text.split("+")

final_text = ""
for ob in initial_text:
    if ob in result_dict:
        final_text += result_dict[ob]
print(final_text)


