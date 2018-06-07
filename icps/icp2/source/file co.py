fh = open(r"txt.txt", "r")

count = 0
data = fh.read()
each_line = data.split("\n")


for i in each_line:
    word = i.split(" ")
    print( " ".join(word), len(word))