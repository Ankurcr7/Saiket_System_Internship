from tkinter import *
import requests
from tkinter import ttk

def crossAmount():
    amountEntry.delete(0,END)

def pressedconvert():

    amount = float(amountEntry.get()) if amountEntry.get()!="" else 0
    
    setfromrate = 0
    settorate =0
    for i in urlDATA:
        if i == fromcombobox.get():
            setfromrate = urlDATA[i]
        
    for j in urlDATA:
        if j == tocombobox.get():
            settorate = urlDATA[j]
        
    
    if fromcombobox.get()!= 'USD':
        rate = "%.3f" % ((amount*settorate)/setfromrate)
    else :
        rate = "%.3f" % (amount*settorate)
    
    convertedamountLabel.config(text= str(amount) + " " + fromcombobox.get() + " = "+ rate + " " + tocombobox.get())


flag = 1 
def reverseCountryCode():
    global flag
    if flag:
        fromcombobox.config(textvariable=totext)
        tocombobox.config(textvariable=fromtext)
        flag = 0
    else:
        fromcombobox.config(textvariable=fromtext)
        tocombobox.config(textvariable=totext)
        flag =1



win = Tk()

KEY = "fca_live_0PQcgMMlfQOoOuXDXxghbYeDEVPGx2SBENXUN04k"

# calling currency exchange API 
url = requests.get("https://api.freecurrencyapi.com/v1/latest?apikey="+KEY)

if url.status_code == 200:
    urlJSON = url.json()
    urlDATA = urlJSON['data'] 

    
else:
    # default data on currency exchange 
    urlDATA = {'AUD': 1.5214101605, 
            'BGN': 1.8171302654, 
            'BRL': 5.1104306438, 
            'CAD': 1.3664802142, 
            'CHF': 0.9094701272, 
            'CNY': 7.2346910187, 
            'CZK': 23.2305829232, 
            'DKK': 6.9487011429, 
            'EUR': 0.931730134, 
            'GBP': 0.7974001341, 
            'HKD': 7.8128009889, 
            'HRK': 6.750360991, 
            'HUF': 362.6715018231, 
            'IDR': 16153.517794785, 
            'ILS': 3.7170305469, 
            'INR': 83.3591366486, 
            'ISK': 139.9265039822, 
            'JPY': 153.0412944114, 
            'KRW': 1363.1109685558, 
            'MXN': 16.9746726515,
            'MYR': 4.7534305623, 
            'NOK': 10.9804818498, 
            'NZD': 1.6763001995,
            'PHP': 57.4774361268,
            'PLN': 4.0362705846, 
            'RON': 4.6366408076, 
            'RUB': 91.9502824519, 
            'SEK': 10.8577617987, 
            'SGD': 1.3532001673, 
            'THB': 36.7906457822, 
            'TRY': 32.4039153547,
            'USD': 1,
            'ZAR': 18.5404429358}
    


height = 360
width  = 640
primaryBG = "#202020"
primaryFG = "white"
secondaryBG = "#303030"
primaryFont = ("sanrif" , 20, "bold")
secondaryFont = ("Courier", 15, "bold")
add_btn_color = "green"
delete_btn_color = "red"

win.minsize(width,height)
win.title("Currency Converter")
win.config(bg = primaryBG) # theme/background_color of the app 



titleLabel = Label(win , text="CURRENCY CONVERTER", fg = primaryFG, bg = primaryBG , font=primaryFont)
titleLabel.pack(pady=20)

entryFrame = Frame(win, width=500, height=30 , bg = primaryBG)
entryFrame.pack()

addLabel= Label(entryFrame , text="Amount:", font=secondaryFont, bg = primaryBG , fg= primaryFG)
addLabel.grid(row=0,column=0, sticky=E)
amountEntry = Entry(entryFrame ,font= secondaryFont, width=30)
amountEntry.grid(row=0,column=1)
cross_btn = Button(entryFrame , text="X" , font= secondaryFont, background= delete_btn_color, overrelief="ridge", cursor="hand2",command=crossAmount )
cross_btn.grid(row=0, column=2, padx=(5,0))

convertFrame = Frame(win, bg = primaryBG)
convertFrame.pack(pady=20)

fromtext = StringVar(value='INR')
totext = StringVar(value='USD')

combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {
                                       'fieldbackground': "black",
                                       'background': 'grey'
                                       }}}
                         )

combostyle.theme_use('combostyle')


countryList =[]
for i in urlDATA:
    countryList.append(i)

countryLabel= Label(convertFrame , text="Country:", font=secondaryFont, bg = primaryBG , fg= primaryFG, )
countryLabel.grid(row=0,column=0,)

fromcombobox = ttk.Combobox(convertFrame, textvariable=fromtext, font=secondaryFont,width=10 , state="readonly", foreground=primaryFG, justify="center",  cursor="hand2",)
fromcombobox['values'] = countryList
fromcombobox.grid(row=0,column=1)


convertLabel= Label(convertFrame , text="=>", font=secondaryFont, bg = primaryBG , fg= primaryFG, )
convertLabel.grid(row=0,column=2, padx=5)


tocombobox = ttk.Combobox(convertFrame, textvariable=totext, font=secondaryFont,width=10, state="readonly", foreground=primaryFG, justify="center",  cursor="hand2" )
tocombobox['values'] = countryList
tocombobox.grid(row=0,column=3)

reverse_btn = Button(convertFrame , text="Revert" , font= secondaryFont, background= "blue" ,overrelief="ridge",  cursor="hand2", command=reverseCountryCode)
reverse_btn.grid(row=0, column=4, padx=5)



convert_btn = Button(convertFrame , text="Convert" , font= secondaryFont, background= add_btn_color ,overrelief="ridge",  cursor="hand2", command=pressedconvert)
convert_btn.grid(row=1, column=0 , columnspan=5,pady=10)


convertedamountFrame = Frame(win, bg=primaryBG)
convertedamountFrame.pack()

convertedamountLabel = Label(convertedamountFrame, text="0 INR = 0.000 USD", font=secondaryFont, bg = primaryBG , fg= primaryFG, )
convertedamountLabel.pack(side=LEFT)

win.mainloop()