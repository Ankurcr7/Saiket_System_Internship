def readfile():
    file = open(path,"r")
    text = file.read().strip()
    textline_list = text.splitlines()
    file.close()
    return text, textline_list


def replace(find_word,replace_word, textline_list):

    new_text_list=[]
    
    flag = False
    for line in textline_list:
        words_list = str(line).split()

        for i in range(len(words_list)):
            if words_list[i][-1] in [".",",","?","!"]:
                if find_word == words_list[i][:-1]:
                    flag = True
                    if flag:
                        words_list[i] = replace_word + words_list[i][-1]

            else:
                if find_word == words_list[i]:
                    flag = True
                    if flag:
                        words_list[i] = replace_word

        new_text_list.append(" ".join(words_list))
    if not flag:
        print("Can't found the word\n")

    text = "\n".join(new_text_list)
    print(text)
    return text

    
def save(text):
    try:
        file = open(path,"w")
        file.write(text)
        
        file.close()
        print("File saved successfully\n")
        print(text)
    
    except:
        print("Saving Failed!")



try:
    path = input("Enter file path(.txt): ").strip()
    print(f"Opening file: {path}\n")
    text, textlines = readfile()
    print(text)
    
    while True:
            
        print("\n1 -> Read File")
        print("2 -> Find and Replace a Word")
        print("3 -> Save")
        print("0 -> Exit")
        options = input("Enter your choice: ")
        if int(options) == 0:
            break

        elif int(options) == 1:
            text = readfile()[0]
            print(text)

        elif int(options) == 2:
            textlines = readfile()[1]
            oldWord = input("Find word: ")
            newWord = input("Replace with: ")
            newText = replace(oldWord,newWord,textlines)

        elif int(options) == 3:
            save(newText)

                
        else:
            print("Invalid choice!\n")

except:
    print("No such file exists!")

