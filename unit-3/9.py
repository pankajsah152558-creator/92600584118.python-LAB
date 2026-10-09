
import re

text = "Python is easy. Python is powerful. I love Python."

# 1. Using match()
result1 = re.match("Python", text)
if result1:
    print("Match:", result1.group())
else:
    print("No match found at the beginning")

# 2. Using search()
result2 = re.search("easy", text)
if result2:
    print("Search:", result2.group())
else:
    print("Pattern not found")

# 3. Using findall()
result3 = re.findall("Python", text)
print("Findall:", result3)
