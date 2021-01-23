import requests
from bs4 import BeautifulSoup
import fake_headers
import tkinter

main = tkinter.Tk()

main.title("TikTok")

main.geometry("150x180")

u1 = str()
curRow = 1

listOBoxU = []
ind = 3

user = tkinter.Entry(master=main)
user.grid(row=curRow)
listOBoxU.append(user)

if "@" in user.get():
    j = user.get().split("@")
    user = j[1]

headers = fake_headers.Headers().generate()

def addu():
    global curRow
    curRow += 1
    user = tkinter.Entry()
    user.grid(row=curRow)
    listOBoxU.append(user)

def lookup():
    global ind
    for uu in listOBoxU:
        with requests.Session() as sess:
            site = sess.get("https://tiktok.com/@"+str(uu.get()),headers=headers)
            soup = BeautifulSoup(site.content,"html.parser")
            try:
                final = (soup.find("strong",attrs={"title":"Followers"}))
                print("Followers :"+str(final.text))
                tkinter.Label(master=main,text=final.text+" Followers").grid(row=curRow+ind)
                ind += 1
            except:
                tkinter.Label(master=main, text="Account not found or account is private").grid(row=ind+4)


addBox = tkinter.Button(master=main,text="Add User",command=addu)
addBox.grid(row=ind+6)

button = tkinter.Button(text="GO!",master=main,command=lookup)

button.grid(row=ind+5)

main.mainloop()