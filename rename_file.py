import os

for f in os.listdir("."):
    if " " in f:
        new_name = f.replace(" ", "_")
        os.rename(f, new_name)