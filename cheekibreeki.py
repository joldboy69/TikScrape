import requests
from bs4 import BeautifulSoup
import fake_headers
import tkinter

main = tkinter.Tk()

main.title("TikTok")

main.geometry("150x180")

user = tkinter.Entry(master=main)

user.grid(row=1)

if "@" in user.get():
    j = user.get().split("@")
    user = j[1]

headers = fake_headers.Headers().generate()
def lookup():
    with requests.Session() as sess:
        site = sess.get("https://tiktok.com/@"+str(user.get()),headers=headers)
        soup = BeautifulSoup(site.content,"html.parser")
        try:
            final = (soup.find("strong",attrs={"title":"Followers"}))
            print("Followers :"+str(final.text))
            tkinter.Label(master=main,text=final.text+" Followers").grid(row=3)
        except:
            tkinter.Label(master=main, text="Account not found or account is private").grid(row=3)


button = tkinter.Button(text="GO!",master=main,command=lookup)

button.grid(row=2)

main.mainloop()
