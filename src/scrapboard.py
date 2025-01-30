import os

location = "./folder/"
filename = "te.st.md"
filename_split = filename.rsplit(".", 1)
location = os.path.join(location, filename_split[0]) + "." + "html"
print(location)