f = open("file.txt", "r") # w = write and r = read


for line in f:
    print(line.strip()) # strip() removes the newline character at the end of each line

f.close() # close the file