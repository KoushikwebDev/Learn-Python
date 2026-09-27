str = "Hello 'Koushik'"
print(str)

# Heading: Strings are immutable 🚀🚀🚀

# Multuline String
str2 = """Hello 
Koushik 
How 
are 
you
"""

print(str2)


str3 = "Hello\nKoushik\n"
print(str3)


# iNdexing
print(str[2])  # * => l


# ? for loop with string

for char in str2:
    print(char)


# ? String Length
print(len(str2))


# ? Check word present in string or not

str4 = "Koushik Saha How are You"
print("Saha" in str4)  # True
print("Saha" not in str4)  # False


# ? String Slice
b = "Hello, World!"

# * from: before to
print(b[2:6])  # * it prints from index 2 to before index 6 => llo,
print(b[:3])  # * it prints first 3 char => Hel
print(b[3:])  # * It print all string from index 3 , => lo, World!
print(b[-5:-2])  # * it prints from last and remove !d from last => orl
print(b[-5:])  # *  it prints => orld!
print(b[:])  # * => print([0:len(b)]) => Hello, World!


# ? Lower case upper case , replace, split && remove white space

a = " Hello Python "
print(a.lower())
print(a.upper())
print(a.strip())  # * removes white space from begining and end

print(a.replace("H", "h"))  # * it return new string, does not modify original string
print(a.split(" "))  # * it converts into list

aa = " Hello!!!!"
print(aa.rstrip("!"))  # * => Hello => it dont remove white space

heading = "introduction to python"
print(heading.capitalize())  # * => Introduction to python

print(heading.center(len(heading) * 2))

# ? count
count = "K K Ssaha"
print(count.count("K"))  # * => 2 => K appeared 2 times in count string

print(aa.endswith("!"))  # * => True

# ? find and index
find = "Koushik is a good bod"
print(find.find("good"))  # * => 13 , it returns index no. if found, else returns -1

print(find.index("Koushik"))  # * => 0

# ? isLower and isUpper and isPrintable, istitle, title
ab = "helllo fotka"
print(ab.islower())  # *=> True
print(ab.isprintable())  # * => True
print(ab.istitle())  # * => False
print(ab.isupper())  # * => False
print(ab.title())  # * => Hello Fotka


# ? String Format
age = 34
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
