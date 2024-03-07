import os

def files(a):
    
    if not os.path.exists(a):
        print("this path is unreal")
        return 
        
    directories = []
    files = []

    for entry in os.listdir(a):
        aa = os.path.join(a, entry)
        if os.path.isdir(aa):
            directories.append(entry)
        elif os.path.isfile(aa):
            files.append(entry)

    return directories, files


a = input("enter path to files and directvories: ")
directories, files = files(a)
print("\ndirectories:")
for directory in directories:
    print(directory)

print("\nfiles:")
for file in files:
    print(file)

