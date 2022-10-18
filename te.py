import re
origional_str="I LOVE CODESPEEDY"
new_str=re.sub("\s","-",origional_str)
print(new_str)