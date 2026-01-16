import os
import shutil

files = os.listdir()

# create new folder
if "text_files" not in files:
    os.mkdir("text_files")

for f in files:
    if f.endswith(".txt"):
        shutil.move(f, "text_files")

print("Task completed")
