import requests
from bs4 import BeautifulSoup
from tkinter import *

def fetch():
    url  = requests.get("https://indianexpress.com/") # news website 

    if  url.status_code == 200: # a successfull response comes with 200 status code
        soup = BeautifulSoup(url.content, "html.parser")

        # finding the top news 
        top = soup.find_all("div", attrs={"class":"content-txt"})
        topnews = ""
        for news in top:
            topnews += news.h3.a.text + "\n\n"

        topLabel.config(text=topnews, justify="left")

        # finding the latest news 
        latest  = soup.find("div", attrs={"class": "top-news"}).find_next("div",attrs={"class": "top-news"}).find("ul").find_all("li")

        latestnews = ""
        for news in latest:
            latestnews += news.h3.a.text + "\n\n"

        latestLabel.config(text=latestnews, justify="left")

        newstop.grid(row=0,column=0,pady=10, sticky="w")
        newslatest.grid(row=0,column=0, pady=10, sticky="w")
        titleLabel.config(text="NEWS SCRAPER",)

    else:
        titleLabel.config(text="Can't load the News")


win = Tk()
height = 840
width  = 1440
primaryBG = "#202020"
primaryFG = "white"
secondaryBG = "#303030"
primaryFont = ("sanrif" , 20, "bold")
secondaryFont = ("Courier", 15, "bold")
arialFont = ("Arial" , 10 ,"bold")
refreshBtnColor = "blue"


win.minsize(width,height)
win.title("News Scraper")


win.config(bg = primaryBG)

titleLabel = Label(win , text="NEWS SCRAPER", fg = primaryFG, bg = primaryBG , font=primaryFont, relief="raised")
titleLabel.pack(pady=20)

mainFrame = Frame(win,  bg = primaryBG)
mainFrame.pack()

leftFrame = Frame(mainFrame, width=(width//2)-40, height=(height)-180 ,bg = primaryBG ,)
rightFrame = Frame(mainFrame, width=(width//2)-40, height=(height)-180 , bg = primaryBG ,)
leftFrame.pack(side="left",padx=15, fill=Y)
rightFrame.pack(side="right",padx = 15, fill=Y)


topLabel = Label(leftFrame, font=arialFont,wraplength=(width//2)-60, bg = primaryBG , fg=primaryFG)
topLabel.grid(row=1,column=0)
newstop = Label(leftFrame, font=primaryFont, bg = primaryBG , fg="red", text="TOP NEWS:-")

latestLabel = Label(rightFrame, font=arialFont,wraplength=(width//2)-60,bg = primaryBG , fg =primaryFG)
latestLabel.grid(row=1,column=0)
newslatest = Label(rightFrame, font=primaryFont, bg = primaryBG , fg="red", text="LATEST NEWS:-")

fetch()
refreshBtn = Button(win, text="Refresh" , font= secondaryFont, background= refreshBtnColor , activebackground="light blue",overrelief="ridge", cursor="hand2", command=fetch)
refreshBtn.pack()




win.mainloop()