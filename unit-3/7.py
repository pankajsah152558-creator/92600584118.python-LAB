
import shutil
import os

# Create a sample file
with open("sample.txt", "w") as f:
    f.write("Hello Python!")

print("File created successfully")

# 1. Copy the file
shutil.copy("sample.txt", "copy.txt")
print("File copied successfully")

# 2. Move the file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully")

# 3. Delete the file
os.remove("moved.txt")
print("File deleted successfully")

# Delete the original file
os.remove("sample.txt")
print("Original file deleted successfully")
