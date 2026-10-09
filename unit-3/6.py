
import os
import sys

# Display current working directory
print("Current Directory:", os.getcwd())

# Create a directory
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully")

# Create and write to a file
with open("MyFolder/sample.txt", "w") as f:
    f.write("Hello Python!\n")
    f.write("File handling using os and sys modules.")

print("File created successfully")

# Read the file
with open("MyFolder/sample.txt", "r") as f:
    print("File Content:")
    print(f.read())

# List files and directories
print("Directory Contents:", os.listdir("MyFolder"))

# Display Python version
print("Python Version:", sys.version.split()[0])

# Display command-line arguments
print("Command-line Arguments:", sys.argv)

# Rename the file
os.rename("MyFolder/sample.txt", "MyFolder/newfile.txt")
print("File renamed successfully")

# Remove the file and directory
os.remove("MyFolder/newfile.txt")
os.rmdir("MyFolder")
print("File and directory removed successfully")
