import re   #import regular expression library

print re.findall(r"[0-9][0-9]", "July 28, 1821")
print re.findall(r"[0-9][0-9]", "12345")
