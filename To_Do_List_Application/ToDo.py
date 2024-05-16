from tkinter import *


def crossTODO():
    todoEntry.delete(0,END)


def crossDesc():
    descEntry.delete(0,END)


index=0
def ADD():
    global index
    todo_value = todoEntry.get().strip()
    desc_value = descEntry.get().strip() if descEntry.get().strip() != "" else "No Description"
    if todo_value !="":
        listbox.insert(index, f"{todo_value} - {desc_value}")
        index+=1


def delete():
    selected_index = listbox.curselection()
    if selected_index!=():
        listbox.delete(selected_index)

def deleteALL():
    listbox.delete(0,END)


checkEmojiUnicode = "\U00002713"  # tick emoji
def complete():
    i = listbox.curselection()
    if i!=():
        text = listbox.get(i)
        if not checkEmojiUnicode in text:
            listbox.delete(i)
            listbox.insert(i, text + " "+ checkEmojiUnicode)  


toggle_mode = True
def toggleMode():
    global toggle_mode
    if toggle_mode:
        win.config(bg = primaryFG)
        entryFrame.config(bg= primaryFG)
        titleLabel.config(fg = primaryBG, bg = primaryFG )
        addLabel.config(bg = primaryFG , fg= primaryBG)
        listbox.config(bg= primaryFG, fg = primaryBG)
        mode_btn.config(text="Dark", bg = primaryBG , fg= primaryFG)
        descLabel.config(bg = primaryFG , fg= primaryBG)
        toggle_mode = False
    else:
        mode_btn.config(text="Light", bg = primaryFG , fg= primaryBG)
        addLabel.config(bg = primaryBG , fg= primaryFG)
        descLabel.config(bg = primaryBG , fg= primaryFG)
        win.config(bg = primaryBG)
        listbox.config(bg= secondaryBG, fg = primaryFG)
        entryFrame.config(bg= primaryBG)
        titleLabel.config(fg = primaryFG, bg = primaryBG )
        toggle_mode = True




win = Tk()

height = 720
width  = 1080
primaryBG = "#202020"
primaryFG = "white"
secondaryBG = "#303030"
primaryFont = ("sanrif" , 20, "bold")
secondaryFont = ("Courier", 15, "bold")
add_btn_color = "green"
delete_btn_color = "red"

win.minsize(width,height)
win.title("ToDo Application")




win.config(bg = primaryBG) # theme/background_color of the app 


titleLabel = Label(win , text="TODO APP", fg = primaryFG, bg = primaryBG , font=primaryFont)
titleLabel.pack(pady=20)

entryFrame = Frame(win, width=500, height=30 , bg = primaryBG)
entryFrame.pack()

addLabel= Label(entryFrame , text="TODO:", font=secondaryFont, bg = primaryBG , fg= primaryFG)
addLabel.grid(row=0,column=0, sticky=E)
todoEntry = Entry(entryFrame , font= secondaryFont, width=30)
todoEntry.grid(row=0,column=1)
cross_btn = Button(entryFrame , text="X" , font= secondaryFont, background= delete_btn_color, overrelief="ridge", command=crossTODO, cursor="hand2")
cross_btn.grid(row=0, column=2, padx=(5,0))

descLabel= Label(entryFrame , text="Description(if any):", font=secondaryFont , fg = primaryFG , bg = primaryBG)
descLabel.grid(row=1,column=0)
descEntry = Entry(entryFrame , font= secondaryFont, width=30)
descEntry.grid(row=1,column=1)
cross_btn = Button(entryFrame , text="X" , font= secondaryFont, background= delete_btn_color, overrelief="ridge", command=crossDesc, cursor="hand2")
cross_btn.grid(row=1, column=2, padx=(5,0))


add_btn = Button(entryFrame, text="ADD" , font= secondaryFont, background= add_btn_color , activebackground="light green",overrelief="ridge", command=ADD, cursor="hand2")
add_btn.grid(row=2, column=0, columnspan=3, sticky=S, pady=5)

mode_btn= Button(entryFrame, text="Light", font = secondaryFont,overrelief="ridge",cursor="hand2", command=toggleMode)
mode_btn.grid(row=2, column=1, sticky=E, pady=5)



listFrame = Frame(win ,bd= 2, relief=SUNKEN , bg = secondaryBG )
listFrame.pack(pady=10)

listbox_scroll_y = Scrollbar(listFrame, orient="vertical")
listbox_scroll_x = Scrollbar(listFrame,orient="horizontal")

listbox = Listbox(listFrame,activestyle="none" ,width=70, height=15, xscrollcommand=listbox_scroll_x.set ,yscrollcommand=listbox_scroll_y.set, font=secondaryFont, cursor="hand2", bg= secondaryBG, fg = primaryFG)

# the ordering is the main thing to do in this frame to set the x-y axis scrollbar
listbox_scroll_x.pack( side=BOTTOM, fill=X)
listbox.pack(fill=BOTH,side=LEFT)
listbox_scroll_y.pack( fill=Y, side=LEFT)

listbox_scroll_y.config(command=listbox.yview)
listbox_scroll_x.config(command=listbox.xview)




buttonsFrame = Frame(win, )
buttonsFrame.pack()
complete_btn = Button(buttonsFrame , text="Complete" , font= secondaryFont, background= add_btn_color ,overrelief="ridge", command=complete, cursor="hand2")
complete_btn.pack( side=LEFT,expand=True, fill= "x")
delete_btn = Button(buttonsFrame , text="Delete" , font= secondaryFont, background= add_btn_color ,overrelief="ridge", command=delete, cursor="hand2")
delete_btn.pack( side=LEFT, expand=True,fill="x")
deleteALL_btn = Button(buttonsFrame , text="Delete ALL" , font= secondaryFont, background= add_btn_color ,overrelief="ridge", command=deleteALL, cursor="hand2")
deleteALL_btn.pack( side=LEFT, expand=True,fill="x")



win.mainloop()