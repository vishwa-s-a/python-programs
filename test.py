import re
str="Janice is 22 and Theon is 33"
ages=re.findall(r"[0-9]{1,2}",str)
names=re.findall(r"[A-Z][a-z]+",str)
if(re.search("Jancy",str)):
    print("Janice is present in meeting")
print(ages)
print(names)