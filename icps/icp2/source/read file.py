filepath = 'txt.txt'
with open(filepath) as fp:
    with open("Sample1.txt", "w") as fp1:
     for line in fp:
        length = str(len(line.strip()))
        line1 = line.strip()+',' + length
        print(line1)
        fp1.write(line1)
        fp1.write("\n")