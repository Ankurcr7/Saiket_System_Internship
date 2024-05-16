def read_words():
    file = open(path, "r")
    words = file.read().strip().split()
    print("Number of Words:",len(words))
    file.close()


def read_lines():
    file = open(path, "r")
    lines = file.readlines()
    # lines = file.read().strip().splitlines()

    print("Number of lines:",len(lines))
    file.close()


def read_characters():
    file = open(path, "r")
    char = file.read()
    print("Number of Characters:",len(char))
    file.close()


def check_frequency():
    file = open(path, "r")
    words:list = file.read().strip().split()
    for x in range(len(words)):
        if words[x][-1] in [".",",","?","!"]:
            words[x]=words[x][:-1]

    print("\nfrequency of each words are :-\n")
    for i in list(set(words)):  # use set(in build function) to remove duplicates
        fre = words.count(i)
        print(i,fre, sep=" - ")
    

    file.close()


try:
    path = input("Enter file path(.txt): ").strip()
    read_words()
    read_lines()
    read_characters()
    check_frequency()

except:
    print("Can't run the program!")