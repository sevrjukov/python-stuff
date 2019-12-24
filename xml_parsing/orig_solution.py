def valid_test(d):
    tag = 0
    slash = 0
    n = []  # seznam tagu
    for i in range(len(d)):
        if d[i] == "<":
            start = i
        elif d[i] == "/":
            slash = i
        elif d[i] == ">":
            end = i
            if slash == 0:
                n.append(d[(start + 1):end])
            elif slash == (end - 1):
                tag += 1
            elif slash == (start + 1):
                slash = 0
                valid = n.pop()
                tag += 1
                if valid != d[(start + 2):end]:
                    print("text nevalidni")
                    exit()
    print("pocet tagu: ", tag, "\ntext validni ")

download = open("texthw04.txt", "r+")
d = download.read()
valid_test(d)