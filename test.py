import os
os.chdir("/home/james/Desktop/")

syntax = 'solve-field --scale-units arcsecperpix --scale-low 6.000 --scale-high 7.000 2020-01-07--05-02-11--418.jpg --out "none" --overwrite'

os.system(syntax)

rtn = os.popen(syntax).read()

## split new line character
rtn_list = rtn.split("\n")
results_list = []

for item in rtn_list:
    if "Field 1 did not solve" not in item:
        results_list.append(item)


solution_values = []
    
for item in results_list:
    if 'Field' in item:
        if "RA" in item or "Dec" in item or "size" in item or "rotation" in item:
            solution_values.append(item)
           
values = []  
            
for it in solution_values:
    if '=' in it:
        # print((it.split('=')))
        values.append(it.split('=')[-1])
    elif ':' in it:
        # print(it.split(":"))
        values.append(it.split(':')[-1])
    
line = ''
for value in values:
    line = line + value + '   '
    

f = open("test3.txt", 'a')
f.write(line)
f.write('\n')
f.close()