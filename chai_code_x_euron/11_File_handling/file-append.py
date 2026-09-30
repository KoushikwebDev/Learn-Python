f = open("file.txt", "a") # a = append and r = read


f.write("This is an appended line.\n")
f.close() # close the file


# write multiple lines using writelines()
lines = ["This is the first appended line.\n", "This is the second appended line.\n"]
f = open("file.txt", "a")
f.writelines(lines)
f.close() # close the file