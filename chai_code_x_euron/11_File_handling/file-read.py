f = open("file.txt", "r") # w = write and r = read


print(f.read())

print(f.read(5)) # read 5 characters

print(f.readline()) # read a line

print(f.readlines()) # read all lines

f.close() # close the file