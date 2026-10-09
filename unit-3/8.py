
import re

text = "Python is easy. Python is powerful."

# 1. Search for a pattern
result = re.search("easy", text)
if result:
    print("Pattern found:", result.group())

# 2. Find all occurrences
matches = re.findall("Python", text)
print("All matches:", matches)

# 3. Match at the beginning
result = re.match("Python", text)
if result:
    print("Match at beginning:", result.group())

# 4. Replace a pattern
new_text = re.sub("Python", "Java", text)
print("After replacement:", new_text)

# 5. Check digits in a string
data = "My age is 18"
digits = re.findall(r"\d+", data)
print("Digits found:", digits)
