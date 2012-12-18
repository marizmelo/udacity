import re

#maximum munch
#regex should match the biggest string that it can not small parts
print re.findall(r"[0-9]+", "13 from 1 in 1776")
#>>> ["13","1","1776"]