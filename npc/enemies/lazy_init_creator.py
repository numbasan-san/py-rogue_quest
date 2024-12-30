import os

list_files = (os.listdir())
files_names = []
for i in list_files:
    if i[0] != '_':
        if not('lazy' in i): files_names.append(i.replace('.py', ''))
print(files_names)
a = files_names
for init in files_names:
    print(f'{init}.{init.capitalize()},')
