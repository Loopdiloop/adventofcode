
#Current dir, for cd-commands
pwd = ["."]

#Record all dir total paths, even without files
dir_paths = ["."]

#For the dir_sizes later
dir_sizes = dict()

#Files, full path of all files mapped to their sizes
files = dict()

def list_to_path(pwd_list):
    """ Convert a list of a pwd to a str path with separator """
    full_path="."
    for p in pwd_list[1:]:
        full_path += "/" + p
    return full_path

#Open file and parse
with open("input.txt") as f:
    for line in f:

        l = line.strip("\n")
        l = l.split(" ")
        
        if l[0] == "$" and l[1] == "ls":
            continue
            
        elif l[0] == "$" and l[1] == "cd":
            if l[2] == "/":
                pwd=["."]
            elif l[2] == "..":
                pwd=pwd[:-1]
            else:
                pwd.append(l[2])
            
        elif l[0] == "dir":
            dir_paths.append(list_to_path(pwd + [l[1]]))
            
        else: #file
            try:
                int(l[0])
            except:
                assert False
            #Add file and size to dict.
            
            full_path = list_to_path(pwd)
            if full_path not in dir_paths:
                print(full_path, " not in dir_paths?!")
                assert False
            
            if not full_path in files.keys():
                files[full_path] = int(0)
            
            files[full_path+"/"+l[1]] = int(l[0])
            

for dir in dir_paths:
    dir_sizes[dir] = 0
    for file in files.keys():
        if dir+"/" in file:
            dir_sizes[dir] += files[file] #add size for all files that share path.

sum_small_dirs = 0
for dirs in dir_sizes.keys():
    if dir_sizes[dirs] <= 100000:
        sum_small_dirs += dir_sizes[dirs]

print("Sum? S1: ", sum_small_dirs)


total_disk = 7e7
disk_space_needed = 3e7
used_space = dir_sizes["."]
free_space = total_disk - used_space
print("Total disk: ", int(total_disk*1e-6), "MB")
print("Free: ", int(free_space)*1e-6, "MB")
print("Used: ", int(used_space)*1e-6, "MB")

additional_space_needed = int(disk_space_needed-(total_disk - used_space))
print("Additional space needed:", additional_space_needed*1e-6, "MB")
deletion_canididates = []

for dirs in dir_sizes.keys():
    if dir_sizes[dirs] >= additional_space_needed:
        deletion_canididates.append(dir_sizes[dirs])

print("S2?: ", min(deletion_canididates))
